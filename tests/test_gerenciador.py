# Estes testes tem o objetivo que a API volte o codigo 200,
# retorna uma lista em json e que esta lista tem um conteudo
from fastapi import status
from fastapi.testclient import TestClient

from gerenciador_tarefas.gerenciador import TAREFAS, app


# definindo uma função de testes
def test_quando_listar_tarefas_devo_ter_como_retorno_codigo_de_status_200():
    # criando um cliente de testes
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    # o verbo get traz a lista de tarefas que estou solicitando
    assert (
        resposta.status_code == status.HTTP_200_OK
    )  # checar se a expresão == é igual e traz resposta


def test_quando_listar_tarefas_formato_de_retorno_deve_ser_json():
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    assert (
        resposta.headers["Content-Type"] == "application/json"
    )  # a resposta do cabeçalho seja do tipo json


def test_quando_listar_tarefas_retorno_deve_ser_uma_lista():
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    assert isinstance(resposta.json(), list)


# funcção isinstance do python verifica se é uma lista,
# pega a resposta e transforma este valor em formato json em uma lista
def test_quando_listar_tarefas_a_tarefa_retornada_deve_possuir_id():
    TAREFAS.append(
        {
            "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "titulo": "titulo 1",
            "descricao": "descricao 1",
            "estado": "finalizado",
        }
    )
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    assert "id" in resposta.json().pop()
    # aqui eu tive como resposta uma lista de tarefas e
    # estou pegando o primeiro elemento da lista que esta no ID
    TAREFAS.clear()
