# TaskFlow API

API de gerenciamento de tarefas desenvolvida com Python e FastAPI.

## Tecnologias utilizadas

- Python
- FastAPI
- Pydantic
- Uvicorn

## Funcionalidades

- Criar tarefas
- Listar tarefas
- Buscar tarefa por ID
- Marcar tarefa como concluída
- Excluir tarefa
- Documentação automática com Swagger

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

- Integração com PostgreSQL
- Docker
- GitHub Actions
- Testes automatizados