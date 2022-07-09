from fastapi import FastAPI # importando a fastApi

app = FastAPI() # criando a aplicação do zero
TAREFAS = []
# "@" é uma forma de vincular esta função listar com o verbo get no recurso de tarefas
@app.get("/tarefas")
def listar(): 
        return TAREFAS
