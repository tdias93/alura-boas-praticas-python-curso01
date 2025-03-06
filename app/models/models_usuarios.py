# Modelo base para um usuário
from pydantic import BaseModel


class Usuario(BaseModel):
    id: int
    nome: str
