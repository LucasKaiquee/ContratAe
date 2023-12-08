"""
Servidor
"""
import pickle
import socket
import threading

from DataStructures.ChainingHashTable import ChainingHashTable 
from DataStructures.ListaSequencialNumPY import Lista
from loguru import logger
from users import Candidato, Recrutador
from vaga import Vaga
from database import CandidatoDB  # , RecrutadorDB, VagaDB

# from vaga import Vaga

HOST = '0.0.0.0'
PORT = 5000

print("=== Servidor ===\n")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
TableCandidatos = ChainingHashTable()
TableRecrutadores = ChainingHashTable()
ListaVagas = []

def get_candidatos_from_db() -> None:
    """Retornando os dados da tabela candidato para a hashtable-candidato"""
    candidatos = CandidatoDB()
    data = candidatos.get_all_candidato()

    candidato_dict = {}

    for i, candidate in enumerate(data):  # manter o i ao lado do for
        lista_candidatos = candidate
        candidato_dict = {"cpf": str(lista_candidatos[0]),
                          "nome": lista_candidatos[1],
                          "email": lista_candidatos[2],
                          "senha": lista_candidatos[3],
                          "skills": lista_candidatos[4],
                          "area": lista_candidatos[5],
                          "descricao": lista_candidatos[6],
                          "cidade": lista_candidatos[7],
                          "uf": lista_candidatos[8],
                        }

        TableCandidatos[candidato_dict["cpf"]] = Candidato(
            candidato_dict["nome"],
            candidato_dict["email"],
            candidato_dict["senha"],
            candidato_dict["cpf"],
            candidato_dict["skills"],
            candidato_dict["area"],
            candidato_dict["descricao"],
            candidato_dict["cidade"],
            candidato_dict["uf"],
        )

    # print(TableCandidatos)
    return logger.info('Candidatos inseridos na HashTable')

def handle_client(cliente):

    # while True:
        # print(cliente)
        protocol_msg = cliente.recv(1024)
        # protocol_msg = protocol_msg.decode('utf-8')
        protocol_msg = pickle.loads(protocol_msg)
        # t2 = threading.Thread(target=protocol, args=(protocol_msg,cliente,))
        # t2.start()
        protocol(protocol_msg, cliente)

def recrutador():
    pass

def candidato(data_cliente):
    user_candidato = TableCandidatos[data_cliente["cpf"]]  # -> recuperando a referencia do objeto candidato
    if user_candidato:
        return user_candidato # -> enviando a referencia do objeto para o cliente
    else:
        return None

def protocol(protocol_msg, cliente):
    """
    GET -> Pegar informações de candidaturas, informações de vagas e lista de candidatos (caso Recrutador).
    POST -> Postar informações como vaga, novo usuário ou recrutador.
    DELETE -> Deletar usuários (Recrutador e Candidato) e vagas.
    UNAPPLY -> Retira a candidatura de uma vaga.
    APPLY -> Referente ao usuário candidatar-se a uma vaga.
    """
    if protocol_msg == 'GET':
        while True:
            print("entrei", protocol_msg)
            data_cliente = pickle.loads(cliente.recv(1024))
        
            if data_cliente["type"] == "c":
                if data_cliente['action'] == 'login':
                    user_candidato = candidato(data_cliente)
                    if user_candidato:
                        if user_candidato.senha == data_cliente["senha"]:
                            protocol_response = {"status": "200 Ok", "data": user_candidato}
                            cliente.send(pickle.dumps(protocol_response))
                            handle_client(cliente)
                            break
                        else:
                            protocol_response = {"status": "401 Unauthorized", "message": "Senha inválida !"}
                    else:
                        protocol_response = {"status": "404 Not Found", "message": "Usuário não encontrado !"}
                    
                    cliente.send(pickle.dumps(protocol_response))

                elif data_cliente['action'] == 'verVagas':
                    if len(ListaVagas) == 0:
                        protocol_response = {"status": "404 Not Found", "message": 'Não há vagas...'}
                        cliente.send(pickle.dumps(protocol_response))
                        handle_client(cliente)
                        break
                    else:
                        protocol_response = {"status": "200 OK", "data": ListaVagas}
                        cliente.send(pickle.dumps(protocol_response))
                        handle_client(cliente)
                        break

            else:
                # protocol_response = recrutador(data_cliente)
                # cliente.send(pickle.dumps(protocol_response))
                pass
            
    elif protocol_msg == 'POST':
        while True:
            print("entrei", protocol_msg)
            data_cliente = cliente.recv(1024) # data_cliente -> dicionario envidado do cliente para o servidor com as informaÃ§Ãµes de tipo e cada campo de acordo com o tipo
            data_cliente = pickle.loads(data_cliente) # -> usando o pickle para decodificar o dicionario
            
            if str(data_cliente["type"]) == "c":
                if data_cliente['action'] == 'criar':
                    if data_cliente["cpf"] not in TableCandidatos:
                        TableCandidatos[data_cliente["cpf"]] = Candidato(
                            data_cliente["nome"], data_cliente["email"], data_cliente["senha"], data_cliente["cpf"])
                        
                        user_candidato = TableCandidatos[data_cliente["cpf"]]
                        logger.info(f'{user_candidato}')
                        protocol_response = {"status": '201 Created', "data": user_candidato}
                        cliente.send(pickle.dumps(protocol_response))
                        # print(TableCandidatos)
                        # Inserindo os dados do Candidato no Banco de Dados
                        candidate = CandidatoDB()
                        candidate.insert_candidato(data_cliente["cpf"], data_cliente["nome"],
                        data_cliente["email"], data_cliente["senha"])
                        handle_client(cliente)
                        break
                    
                    else:
                        protocol_response = {"status": "400 Bad Request", "message": "CPF já cadastrado."}
                        cliente.send(pickle.dumps(protocol_response))
                        
                

            elif data_cliente["type"] == "r":
                r = Recrutador(
                    data_cliente["nome"],
                    data_cliente["nomeEmpresa"],
                    data_cliente["senha"],
                    data_cliente["cpf"],
                )

                TableRecrutadores[data_cliente["cpf"]] = r
                
                v = r.criar_vaga('IFPB','TI','dinheiro bom',1,'1300,00', 'cérebro')
                v1 = r.criar_vaga('IFPB JOAO PESSOA','TI','WALTER',10,'1300,00', 'cérebro')
                v2 = r.criar_vaga('CAMPINA GRANDE','TI','vaga para react',10,'1300,00', 'cérebro')


                ListaVagas.append(v)
                ListaVagas.append(v1)
                ListaVagas.append(v2)

                # print(ListaVagas)

    elif protocol_msg == 'APPLY':
        while True:
            print("entrei", protocol_msg)
            data_cliente = cliente.recv(1024) 
            data_cliente = pickle.loads(data_cliente)
            print(data_cliente)

            if data_cliente['type'] == "c":
                logger.info('entrei')
                if data_cliente['action'] == 'candidatar':
                    idVaga = data_cliente['idVaga']
                    for i in ListaVagas:
                        if i.id == idVaga:
                            if i.vagaEstaCheia():
                                protocol_response = {"status": "400 Bad Request", "message":'Limite de candidaturas alcançados.'}
                                cliente.send(pickle.dumps(protocol_response))
                                handle_client(cliente)
                                break
                            else:
                                cand = TableCandidatos[data_cliente["cpf"]]
                                cand.candidatar(i)
                                i.adicionarCandidatura(cand)
                                #SEMAFORO
                                protocol_response = {"status": "200 OK", "message": 'Candidatura registrada com sucesso!'}
                                logger.info(protocol_response["message"])
                                cliente.send(pickle.dumps(protocol_response))
                                handle_client(cliente)
                                break
                        else:
                            protocol_response = {"status":"404 Not Found", "message":'Vaga não encontrada.'}
                            cliente.send(pickle.dumps(protocol_response))

    elif protocol_msg == "UNAPPLY":
        while True:
            print("entrei", protocol_msg)
            data_cliente = cliente.recv(1024) 
            data_cliente = pickle.loads(data_cliente)
            print(data_cliente)

            if data_cliente['type'] == "c":
                logger.info('entrei')
                if data_cliente['action'] == 'cancelarCand':
                    idVaga = data_cliente['idVaga']
                    candi = TableCandidatos[data_cliente["cpf"]]
                    logger.info(candi.vagas_aplicadas)
                    for i in candi.vagas_aplicadas:
                        if i.id == idVaga:
                            indice_remocao = candi.vagas_aplicadas.index(i)
                            candi.cancelar_candidatura(indice_remocao)



                              

def run_server():
    print( 'teste')
    while True:
        cliente, addr = server.accept()
        t1 = threading.Thread(target=handle_client, args=(cliente,))
        t1.start()

# Retornando os dados da tabela candidato para a hashtable-candidato
get_candidatos_from_db()
run_server()

