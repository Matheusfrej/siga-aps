# SigaB

Repositório para o projeto da disciplina Análise e Projeto de Sistemas do Centro de Informática da UFPE

## Projeto

O nosso projeto é o SigaB, um sistema de gerenciamento acadêmico. A descrição mais detalhada do projeto e seus casos de uso estão na pasta Entrega 1

## Organização

- Projeto RUP
O nosso projeto foi organizado em duas pastas principais: frontend e backend. Para executar o servidor, abra a pasta backend e execute **pip install -r requirements.txt** e, após isso, execute **python app.py**. Depois, para executar o frontend, abra a pasta frontend e execute primeiro **npm install** e, por fim, **npm run dev**.

-Projeto SOA
Para executar o projeto em sua versão de SOA, na pasta siga-aps execute o comando **docker-compose build** e **depois docker-compose up**. Isso vai iniciar os containers de todos os microsserviços. Para executar o frontend,abra a pasta frontend e execute primeiro **npm install** e, por fim, **npm run dev**.

## Tecnologias
Nosso backend está em Python, usando o framework Flask e o SQLAlchemy para integrar o banco de dados SQLite. Nosso frontend está em React com TypeScript. Fizemos login com o agente externo Firebase Auth.

## Equipe
- Alice Sales (avss2)
- Bruna Alves (baws)
- FIlipe Gomes (fgm3)
- Matheus Frej (mflc)
