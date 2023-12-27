![Group 17](https://github.com/LucasKaiquee/ContratAe/assets/85175643/ae517df4-87d4-4b9a-8e98-3a653266aef4)

### Bem-vindo(a) ao ContratAe, uma aplicação na arquitetura cliente-servidor dedicada a facilitar a integração entre estudantes em busca de estágio e oportunidades disponíveis. Nosso objetivo é aprimorar a comunicação entre estudantes e empresas, visando superar desafios frequentes relacionados à interação entre faculdades e o setor corporativo.

Neste projeto, utilizamos as seguintes tecnologias:

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-005F9E?style=for-the-badge&logo=supabase&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

## Funcionalidades do Candidato:

1. **Entrar ou Criar Conta:**
2. **Completar Perfil:**
3. **Ver Vagas Disponíveis:**
4. **Candidatar-se a uma Vaga:**
5. **Cancelar Candidatura:**
6. **Ver Perfil:**
7. **Ver Candidaturas Realizadas:**

## Funcionalidades do Recrutador:

1. **Entrar ou Criar Conta:**
2. **Criar Vaga:**
3. **Ver Candidaturas para uma Vaga:**

## Disciplinas Envolvidas:
As funcionalidades do ContratAe são desenvolvidas considerando conceitos e práticas das disciplinas do curso de Sistemas Para Internet do IFPB campus João Pessoa. As principais disciplinas envolvidas são:

### Sistemas Operacionais
- Utilização de Multithreading e Semáforos para proteger regiões críticas.

### Protocolos e Interconexão de Redes
- Implementação da API de sockets para interagir com o servidor através do protocolo de transporte TCP.
- Desenvolvimento de um protocolo de aplicação personalizado.

### Estrutura de Dados
- Utilização das estruturas de dados hashtable e lista encadeada.
- Implementação de tratamento de exceções para aprimorar a robustez do sistema.
  
## Conheça o Protocolo:

Para entender o protocolo SPC utilizado neste projeto e como ele funciona, consulte a documentação detalhada em [protocol_docs.md](protocol_docs.md).

## Estrutura do Projeto:

| Arquivo               | Descrição                                   |
|-----------------------|---------------------------------------------|
| `cliente.py`          | Implementação do cliente                    |
| `servidor.py`         | Implementação do servidor                   |
| `servidorHTTP.py`     | Implementação de um servidor HTTP           |
| `requirements.txt`    | Lista de dependências do projeto            |
| `supabase_db.py`      | Integração com o banco de dados Supabase    |
| `users.py`            | Módulo das clasees dos usuários             |
| `vaga.py`             | Módulo da classe da vaga                    |
| `DataStructures`     | Pasta contendo as estruturas de dados        |

## Dependências:

Certifique-se de instalar as seguintes dependências antes de executar o projeto:

- [Loguru](https://github.com/Delgan/loguru): Uma poderosa biblioteca de logging para Python.
- [Supabase](https://github.com/supabase/supabase-py): Cliente Python para interagir com a plataforma Supabase.
- [python-dotenv](https://github.com/theskumar/python-dotenv): Carrega variáveis de ambiente a partir de um arquivo chamado `.env`.
- [NumPy](https://numpy.org/): Biblioteca para suporte a arrays e matrizes multidimensionais, junto com funções matemáticas de alto nível para operar nesses elementos.

## Instalação das Dependências:

Use o seguinte comando para instalar as dependências:

```bash
pip install -r requirements.txt
```

## Execução:

Inicie o servidor usando o seguinte comando:

```bash
python servidor.py
````

Em seguida, inicie o cliente, passando o IP do servidor como argumento:

```bash
python cliente.py [ip_do_servidor]
```

## Desenvolvedores:

Este projeto foi desenvolvido por:

- Lucas Kaique: [GitHub](https://github.com/LucasKaiquee)<br>
  email :  [kaique.lucas@academico.ifpb.edu.br](mailto:kaique.lucas@academico.ifpb.edu.br)
  
- Luiz Fernando: [GitHub](https://github.com/LuizFernando12)<br>
  email: [fernando.albuquerque@academico.ifpb.edu.br](mailto:fernando.albuquerque@academico.ifpb.edu.br)
  
- Marcelo Bruno: [GitHub](https://github.com/marceelobruno)<br>
  email: [bruno.marcelo@academico.ifpb.edu.br](mailto:bruno.marcelo@academico.ifpb.edu.br) 

## Contribuição:

Este é um projeto acadêmico e não requer contribuições no momento.

## Licença:

Este projeto está licenciado sob a [MIT License](LICENSE).

