from system.cli import MESSAGES
from system.models import cadastrar
from system.database import (
    carregar_dados,
    salvar_dados
)


def anexar_arquivo():
    nova_pessoa = cadastrar()
    dados = carregar_dados()

    if any(p["email"] == nova_pessoa["email"] for p in dados):
        return False, MESSAGES['EMAIL_EXISTS']

    dados.append(nova_pessoa)
    salvar_dados(dados)

    return True, MESSAGES['REGISTER_SUCCESS']


def listar_pessoas():
    dados = carregar_dados()

    if not dados:
        return False, MESSAGES['EMPTY_DATA']

    return True, dados


def remover_alguem(id_procurado):
    dados = carregar_dados()

    if not dados:
        return False, MESSAGES['EMPTY_DATA']

    nova_lista = []
    nome_removido = None

    for pessoa in dados:
        if pessoa['id'] == id_procurado:
            nome_removido = pessoa['nome']
            continue
        nova_lista.append(pessoa)

    if nome_removido is None:
        return False, MESSAGES['ID_NOT_FOUND']

    salvar_dados(nova_lista)
    return True, nome_removido


def search_by_field(field: str):
    data = carregar_dados()
    found_users = list()

    if not data:
        return False, MESSAGES['EMPTY_DATA']

    if field not in ['nome', 'idade']:
        return False, MESSAGES['INVALID_VALUE']

    wanted_value = input(f'{field.capitalize()} da pessoa: ').strip()

    for people in data:
        if str(people[field]).lower() == wanted_value.lower():
            found_users.append(people)

    if found_users:
        return True, found_users

    return False, MESSAGES['USER_NOT_FOUND']
