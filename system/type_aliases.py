from typing import TypedDict

class Pessoa(TypedDict):
    id: str
    nome: str
    idade: int
    email: str
    senha: str

type Pessoas = list[Pessoa]