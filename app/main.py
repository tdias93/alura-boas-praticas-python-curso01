from typing import Dict
from fastapi import FastAPI
from app.routers import routers_usuarios, routers_produtos

# Variável de Mensagem de Boas Vindas
MENSAGE_HOME: str = "Bem-vindo à API de Recomendação de Produtos"

# Criando o App
app = FastAPI()

# Incluindo os Routers
app.include_router(routers_usuarios.router)
app.include_router(routers_produtos.router)


# Iniciando o servidor
@app.get("/")
def home() -> Dict[str, str]:
    global MENSAGE_HOME
    return {"mensagem": MENSAGE_HOME}
