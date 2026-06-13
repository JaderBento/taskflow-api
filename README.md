# TaskFlow API

API REST para gerenciamento de tarefas desenvolvida com Python, FastAPI e PostgreSQL, utilizando Docker para containerização, testes automatizados com Pytest e integração contínua com GitHub Actions.

## Tecnologias Utilizadas

* Python
* FastAPI
* PostgreSQL
* Pydantic
* Uvicorn
* Pytest
* Docker
* GitHub Actions

## Funcionalidades

* Criar tarefas
* Listar tarefas
* Buscar tarefa por ID
* Marcar tarefa como concluída
* Excluir tarefas
* Documentação automática com Swagger
* Persistência de dados com PostgreSQL
* Testes automatizados
* Execução em containers Docker

## Testes Automatizados

O projeto possui testes automatizados utilizando Pytest para validar as principais funcionalidades da API.

## Integração Contínua

Os testes são executados automaticamente através do GitHub Actions a cada novo push realizado no repositório.

## Como Executar

### Método 1 - Execução Local

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a API:

```bash
uvicorn main:app --reload
```

Acesse a documentação:

```text
http://127.0.0.1:8000/docs
```

---

### Método 2 - Execução com Docker

Execute:

```bash
docker compose up --build
```

Acesse a documentação:

```text
http://127.0.0.1:8000/docs
```

## Configuração do Banco de Dados

Crie o banco de dados:

```sql
CREATE DATABASE taskflow;
```

Crie a tabela:

```sql
CREATE TABLE tarefas (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    concluida BOOLEAN DEFAULT FALSE
);
```

## Rotas Disponíveis

### Criar tarefa

```http
POST /tarefas
```

Exemplo:

```json
{
  "titulo": "Estudar Python"
}
```

### Listar tarefas

```http
GET /tarefas
```

### Buscar tarefa por ID

```http
GET /tarefas/{id}
```

### Concluir tarefa

```http
PUT /tarefas/{id}/concluir
```

### Excluir tarefa

```http
DELETE /tarefas/{id}
```

## Estrutura do Projeto

```text
TaskFlow
├── main.py
├── Dockerfile
├── docker-compose.yml
├── init.sql
├── requirements.txt
├── README.md
├── tests
│   └── test_api.py
└── .github
    └── workflows
        └── tests.yml
```

## Aprendizados

Durante o desenvolvimento deste projeto foram aplicados conceitos de:

* Desenvolvimento de APIs REST
* Integração com banco de dados PostgreSQL
* Testes automatizados com Pytest
* Integração contínua com GitHub Actions
* Containerização com Docker
* Controle de versão com Git e GitHub

```
```
