import json
import os
from system import Pessoas

def garantir_pasta() -> None:
    os.makedirs('data', exist_ok=True)

def carregar_dados() -> Pessoas:
    try:
        with open('data/cadastrados.json', 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar_dados(dados: Pessoas) -> None:
    with open('data/cadastrados.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)