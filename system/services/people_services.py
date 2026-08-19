from system import Pessoas, Pessoa
from system.models import verificar_nome, verificar_idade, verificar_email, criar_nova_senha
from system.cli import MESSAGES, show_result, mostrar_pessoas, empty_data, panel
from system.models import cadastrar
from system.database import (
    carregar_dados,
    salvar_dados
)

VALID_FIELDS: set[str] = {"id", "nome", "idade", "email"}

def anexar_arquivo() -> None:
    new_person: Pessoa = cadastrar()
    data: Pessoas = carregar_dados()

    if any(p["email"] == new_person["email"] for p in data):
        show_result(MESSAGES['EMAIL_EXISTS'], "error")
        return

    data.append(new_person)
    salvar_dados(data)
    show_result(MESSAGES["REGISTER_SUCCESS"], "success")


def listar_pessoas() -> None:
    data: Pessoas = carregar_dados()

    if not data:
        empty_data()
        return

    mostrar_pessoas(data)


def remover_alguem() -> None:
    data: Pessoas = carregar_dados()

    if not data:
        empty_data()
        return

    id_procurado: str = input("Digite o id da pessoa que deseja remover: ")

    nova_lista: Pessoas = []
    nome_removido: str | None = None

    for pessoa in data:
        if pessoa['id'] == id_procurado:
            nome_removido = pessoa['nome']
            continue
        nova_lista.append(pessoa)

    if nome_removido is None:
        show_result(MESSAGES['ID_NOT_FOUND'], "error")
        return

    while True:

        choice: str = input(f'Deseja mesmo excluir {nome_removido}? [s/n]').strip().lower()

        if choice == 's':
            salvar_dados(nova_lista)
            panel(f"\nUsuário [blue]{nome_removido}[/] foi removido com sucesso.")
            return

        if choice == 'n':
            panel(f"\nUsuário [blue]{nome_removido}[/] não foi removido com sucesso.")
            return

        show_result('Digite apenas "s" ou "n".', "error")


def search_by_field(field: str) -> None:
    data: Pessoas = carregar_dados()
    found_users: Pessoas = []

    if not data:
        empty_data()
        return

    if field not in ['nome', 'idade']:
        show_result(MESSAGES['INVALID_VALUE'], "error")
        return

    wanted_value: str = input(f'{field.capitalize()} da pessoa: ').strip()

    for person in data:
        if str(person[field]).lower() == wanted_value.lower():
            found_users.append(person)

    if found_users:
        mostrar_pessoas(found_users, True)
        return

    show_result(MESSAGES['USER_NOT_FOUND'], "error")


def sort_by_field() -> None:
    data: Pessoas = carregar_dados()

    if not data:
        empty_data()
        return

    reverse_order: bool = False
    field: str = input("Digite o campo (id, nome, idade, email) para listar em ordem: ").strip().lower()

    if field not in VALID_FIELDS:
        show_result(MESSAGES['INVALID_VALUE'], "error")
        return

    reverse: str = input("Deseja ver em ordem reversa? (s/n): ").strip().lower()

    if reverse == "s":
        reverse_order = True

    people_list = sorted(
        data,
        key=lambda person: person[field],
        reverse=reverse_order
    )

    mostrar_pessoas(people_list, True)


def all_people_function() -> None:
    people: int = len(carregar_dados())

    if people == 0:
        empty_data()
    else:
        print(f'\nHá um total de {people} pessoas cadastradas')


def edit_registration() -> None:
    data: Pessoas = carregar_dados()
    new_list: Pessoas = []

    if not data:
        empty_data()
        return

    proposed_id: str = input('Digite o ID para editar o cadastro: ').strip().lower()

    found: bool = False

    for person in data:
        if proposed_id == person['id']:
            found = True

            edited_person: Pessoa = {
                'id': person['id'],
                'nome': verificar_nome(),
                'idade': verificar_idade(),
                'email': verificar_email(),
                'senha': criar_nova_senha(),
            }
            new_list.append(edited_person)
            continue

        new_list.append(person)

    if not found:
        show_result(MESSAGES["ID_NOT_FOUND"], "error")
        return

    salvar_dados(new_list)
    show_result(MESSAGES['EDIT_SUCCESS'], "success")