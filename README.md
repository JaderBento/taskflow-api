# TaskFlow API

API REST para gerenciamento de tarefas desenvolvida com Python, FastAPI e PostgreSQL, permitindo o gerenciamento persistente de tarefas através de operações CRUD.

## Tecnologias Utilizadas

* Python
* FastAPI
* PostgreSQL
* Pydantic
* Uvicorn
* Pytest
* GitHub Actions

## Funcionalidades

* Criar tarefas
* Listar tarefas
* Buscar tarefa por ID
* Marcar tarefa como concluída
* Excluir tarefas
* Documentação automática com Swagger
* Persistência de dados com PostgreSQL

## Testes Automatizados

O projeto possui testes automatizados utilizando Pytest para validar as principais funcionalidades da API.

## Integração Contínua

Os testes são executados automaticamente através do GitHub Actions a cada novo push realizado no repositório.

## Como Executar

### Instalar dependências

```bash
pip install -r requirements.txt
```

### Executar a API

```bash
uvicorn main:app --reload
```

### Acessar a documentação

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
├── tests
│   └── test_api.py
├── requirements.txt
├── README.md
└── .github
    └── workflows
        └── tests.yml
```

## Próximas Melhorias

* Docker

```
```
