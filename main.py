from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2

app = FastAPI()

conexao = psycopg2.connect(
    host="127.0.0.1",
    database="TaskFlow",
    user="postgres",
    password="sua_senha",
    port="5432"
)

cursor = conexao.cursor()

class Tarefa(BaseModel):
    titulo: str

@app.get("/")
def home():
    return {"mensagem": "TaskFlow API Online com PostgreSQL"}

@app.get("/tarefas")
def listar_tarefas():
    cursor.execute("SELECT id, titulo, concluida FROM tarefas ORDER BY id")
    tarefas = cursor.fetchall()

    return [
        {"id": tarefa[0], "titulo": tarefa[1], "concluida": tarefa[2]}
        for tarefa in tarefas
    ]

@app.post("/tarefas")
def criar_tarefa(tarefa: Tarefa):
    cursor.execute(
        "INSERT INTO tarefas (titulo, concluida) VALUES (%s, %s) RETURNING id, titulo, concluida",
        (tarefa.titulo, False)
    )
    nova_tarefa = cursor.fetchone()
    conexao.commit()

    return {
        "id": nova_tarefa[0],
        "titulo": nova_tarefa[1],
        "concluida": nova_tarefa[2]
    }

@app.get("/tarefas/{id}")
def buscar_tarefa(id: int):
    cursor.execute("SELECT id, titulo, concluida FROM tarefas WHERE id = %s", (id,))
    tarefa = cursor.fetchone()

    if tarefa:
        return {"id": tarefa[0], "titulo": tarefa[1], "concluida": tarefa[2]}

    return {"erro": "Tarefa não encontrada"}

@app.put("/tarefas/{id}/concluir")
def concluir_tarefa(id: int):
    cursor.execute(
        "UPDATE tarefas SET concluida = TRUE WHERE id = %s RETURNING id, titulo, concluida",
        (id,)
    )
    tarefa = cursor.fetchone()
    conexao.commit()

    if tarefa:
        return {"id": tarefa[0], "titulo": tarefa[1], "concluida": tarefa[2]}

    return {"erro": "Tarefa não encontrada"}
@app.delete("/tarefas/{id}")
def excluir_tarefa(id: int):
    cursor.execute("DELETE FROM tarefas WHERE id = %s RETURNING id", (id,))
    tarefa = cursor.fetchone()
    conexao.commit()

    if tarefa:
        return {"mensagem": "Tarefa removida com sucesso"}

    return {"erro": "Tarefa não encontrada"}