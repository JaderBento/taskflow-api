# TaskFlow API

API de gerenciamento de tarefas desenvolvida com Python, FastAPI e PostgreSQL, permitindo o gerenciamento persistente de tarefas através de operações CRUD.

## Tecnologias utilizadas

- Python
- FastAPI
- PostgreSQL
- Pydantic
- Uvicorn

## Funcionalidades

- Criar tarefas
- Listar tarefas
- Buscar tarefa por ID
- Marcar tarefa como concluída
- Excluir tarefa
- Documentação automática com Swagger
- Persistência de dados com PostgreSQL

## Como executar

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
## Configuração do Banco de Dados

Crie um banco PostgreSQL chamado:

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

## Rotas disponíveis

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
GET /tarefas/1
```

### Concluir tarefa

```http
PUT /tarefas/1/concluir
```

### Excluir tarefa

```http
DELETE /tarefas/1
```

## Próximas melhorias

- Docker
- GitHub Actions
- Testes automatizados
