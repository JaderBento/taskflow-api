import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "mensagem" in response.json()


def test_criar_tarefa():
    response = client.post("/tarefas", json={
        "titulo": "Tarefa de teste"
    })

    assert response.status_code == 200

    dados = response.json()

    assert "id" in dados
    assert dados["titulo"] == "Tarefa de teste"
    assert dados["concluida"] == False


def test_listar_tarefas():
    response = client.get("/tarefas")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_buscar_tarefa_por_id():
    criar = client.post("/tarefas", json={
        "titulo": "Buscar tarefa teste"
    })

    tarefa_id = criar.json()["id"]

    response = client.get(f"/tarefas/{tarefa_id}")

    assert response.status_code == 200
    assert response.json()["id"] == tarefa_id


def test_concluir_tarefa():
    criar = client.post("/tarefas", json={
        "titulo": "Concluir tarefa teste"
    })

    tarefa_id = criar.json()["id"]

    response = client.put(f"/tarefas/{tarefa_id}/concluir")

    assert response.status_code == 200
    assert response.json()["concluida"] == True


def test_excluir_tarefa():
    criar = client.post("/tarefas", json={
        "titulo": "Excluir tarefa teste"
    })

    tarefa_id = criar.json()["id"]

    response = client.delete(f"/tarefas/{tarefa_id}")

    assert response.status_code == 200
    assert "mensagem" in response.json()