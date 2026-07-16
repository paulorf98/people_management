from system.cli import MESSAGES
from system.models import cadastrar
from system.database import (
    carregar_dados,
    salvar_dados,
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


def search_name():
    data = carregar_dados()

    if not data:
        return False, MESSAGES['EMPTY_DATA']

    wanted_name = input('Digite o nome da pessoa: ').strip()

    for people in data:
        if people['nome'].lower() == wanted_name.lower():
            return True, people

    return False, MESSAGES['USER_NOT_FOUND']