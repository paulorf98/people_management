import json
import os

def garantir_pasta():
    os.makedirs('data', exist_ok=True)

def carregar_dados():
    try:
        with open('data/cadastrados.json', 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar_dados(dados):
    with open('data/cadastrados.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)