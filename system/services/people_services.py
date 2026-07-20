from system import Pessoas
from system.cli import MESSAGES, empty_data
from system.models import cadastrar
from system.database import (
    carregar_dados,
    salvar_dados
)


def anexar_arquivo() -> tuple[bool, str]:
    nova_pessoa = cadastrar()
    dados = carregar_dados()

    if any(p["email"] == nova_pessoa["email"] for p in dados):
        return False, MESSAGES['EMAIL_EXISTS']

    dados.append(nova_pessoa)
    salvar_dados(dados)

    return True, MESSAGES['REGISTER_SUCCESS']


def listar_pessoas() -> tuple[bool, Pessoas | str]:
    dados = carregar_dados()

    if not dados:
        return empty_data()

    return True, dados


def remover_alguem(id_procurado: str) -> tuple[bool, str]:
    dados = carregar_dados()

    if not dados:
        return empty_data()

    nova_lista = []
    nome_removido: str | None = None

    for pessoa in dados:
        if pessoa['id'] == id_procurado:
            nome_removido = pessoa['nome']
            continue
        nova_lista.append(pessoa)

    if nome_removido is None:
        return False, MESSAGES['ID_NOT_FOUND']

    salvar_dados(nova_lista)
    return True, nome_removido


def search_by_field(field: str) -> tuple[bool, Pessoas | str]:
    data = carregar_dados()
    found_users = list()

    if not data:
        return empty_data()

    if field not in ['nome', 'idade']:
        return False, MESSAGES['INVALID_VALUE']

    wanted_value = input(f'{field.capitalize()} da pessoa: ').strip()

    for person in data:
        if str(person[field]).lower() == wanted_value.lower():
            found_users.append(person)

    if found_users:
        return True, found_users

    return False, MESSAGES['USER_NOT_FOUND']


def sort_by_field(field: str, reverse_order: bool = False) -> tuple[bool, str | Pessoas]:
    data = carregar_dados()

    if not data:
        return empty_data()

    valid_fields = {"id", "nome", "idade", "email", "senha"}

    if field not in valid_fields:
        print("Campo inválido.")
        return False, MESSAGES['INVALID_VALUE']

    people_list = sorted(
        data,
        key=lambda person: person[field],
        reverse=reverse_order
    )

    return True, people_list

