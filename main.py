from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

tarefas = []
contador_id = 1


class Tarefa(BaseModel):
    titulo: str


@app.get("/")
def home():
    return {"mensagem": "TaskFlow API Online"}


@app.get("/tarefas")
def listar_tarefas():
    return tarefas


@app.post("/tarefas")
def criar_tarefa(tarefa: Tarefa):
    global contador_id

    nova_tarefa = {
        "id": contador_id,
        "titulo": tarefa.titulo,
        "concluida": False
    }

    tarefas.append(nova_tarefa)
    contador_id += 1

    return nova_tarefa


@app.get("/tarefas/{id}")
def buscar_tarefa(id: int):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            return tarefa

    return {"erro": "Tarefa não encontrada"}


@app.put("/tarefas/{id}/concluir")
def concluir_tarefa(id: int):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefa["concluida"] = True
            return tarefa

    return {"erro": "Tarefa não encontrada"}


@app.delete("/tarefas/{id}")
def excluir_tarefa(id: int):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefas.remove(tarefa)
            return {"mensagem": "Tarefa removida com sucesso"}

    return {"erro": "Tarefa não encontrada"}