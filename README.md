<h1 align="center">Simple Api Designer | Projet Default com Python e FastAPI</h1>

<p align="justify">Olá, seja bem vindo ao meu repositório padrão, criei esse projeto como padrão 
para implementação de um api utilizando a linguagem Python e biblioteca FastAPI,
meu objetivo é criar um projeto com tecnologias e estrutura padrão para servir de
consulta, pretendo implementar uma API REST integrada as tcnologias mais utilizadas
no mercado de desenvolvimento de software.<br>
Se você for um profissional experiente, poderá sentir falta de alguma coisa ou
que algumas partes do projeto poderia ser melhor, conto com o seu feedback para melhorar
esse código e tornar ele o mais eficiente possível para ajudar a comunidade.</p>

## Estrutura do projeto

- Services: Validar as regra de negócio e validar se o dados que deseja alterar já existe em banco/Incluir arquivo com log
- Repositorys: Faz a interação com o banco de dados
- Models: Possui os modelos cadastrados para estruturar a aplicação e o banco de dados.
- Schemas: Possui os campos que serão esperados nas requisições e input, output, standard(StandardOutput, StandardInput, ErrorOutput, UserOutput).
- Routers: Possui as rotas do serviço.
- infra: database/nosql/queue/aws/external requests

## Tecnologias inclusas neste projeto
- [ ] Python
- [ ] FastAPI/API REST
- [ ] PostgreSQL
- [ ] MongoDB
- [ ] Redis
- [ ] AWS/S3
- [ ] Kafka

## Rodar o serviço
```bash
$ uvicorn main:app --reload
ou
$ uvicorn src.main:app --reload

$ uvicorn src.server:app --reload --reload-dir=src

Saída:
←[32mINFO←[0m:     Will watch for changes in these directories: ['C:\\Users\\User\\PycharmProjects\\fastApi']
←[32mINFO←[0m:     Uvicorn running on ←[1mhttp://127.0.0.1:8000←[0m (Press CTRL+C to quit)
←[32mINFO←[0m:     Started reloader process [←[36m←[1m19836←[0m] using ←[36m←[1mStatReload←[0m
←[32mINFO←[0m:     Started server process [←[36m15920←[0m]
←[32mINFO←[0m:     Waiting for application startup.
←[32mINFO←[0m:     Application startup complete.
```