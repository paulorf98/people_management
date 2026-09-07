from operator import itemgetter
from typing import cast
from uuid import uuid4

from system.cli import cliente as cli
from system.database.storage import save_data
from system.models.person import Person
from system.services.results import EditResult
from system.type_aliases import People, PersonData
from system.utils import people_utils as utils
from system.utils.people_utils import find_person, remove_person_by_id
from system.utils.validation import authenticate


def create_person_flow() -> Person:
    # Verifica os dados informados
    name = cli.ask_name()
    age = cli.ask_age()
    email = cli.ask_email()
    password = cli.ask_password()

    # Cria a pessoa em formato dataclass
    person = Person(
        id=str(uuid4()),
        name=name,
        age=age,
        email=email,
        password=password
    )

    return person


def register(data: People) -> None:
    # Cria a pessoa
    person: Person = create_person_flow()

    # Torna compatível com JSON
    person_data: PersonData = person.to_dict()

    # Verifica se o email já existe
    exists = utils.email_exists(data=data, email=person_data['email'])
    if exists:
        cli.panel(category="erro", key="EMAIL_EXISTS")
        return

    # Adiciona a nova pessoa
    data.append(person_data)

    # Reescreve o JSON e salva o arquivo
    save_data(data)

    cli.panel('sucesso', key='USER_CREATED')


def registered_people(data: People) -> None:

    # Verifica se a lista está vazia
    if not data:
        cli.panel("info", key="EMPTY_DATA")
        return

    # lista as pessoas em formato de tabela
    cli.show_people(data)


def delete_person(data: People) -> None:
    """
    Coordena o fluxo de remoção de uma pessoa.

    Obtém o ID, valida a existência da pessoa,
    solicita confirmação e persiste a remoção.

    :return: None
    """

    person_id = cli.get_person_id()
    found_person = utils.find_person(data, person_id)

    if found_person is None:
        cli.panel(category="info", key="ID_NOT_FOUND")
        return

    password = cli.get_password()

    valid_password = authenticate(found_person, password)

    if not valid_password:
        cli.panel("erro", text="INCORRECT_PASSWORD")
        return

    confirm = cli.confirm(
        f"Deseja mesmo excluir {found_person['name']}? S/N: "
    )

    if not confirm:
        cli.panel(
            "info",
            text=f"A remoção de {found_person['name']} foi cancelada "
                 f"e o usuário não foi deletado."
        )
        return

    updated_data = utils.remove_person_by_id(data, person_id)
    save_data(updated_data)
    cli.panel(category="sucesso", key="PERSON_REMOVED")


def search_people(data: People) -> People | None:

    # Obtém o campo
    field = cli.get_valid_field()

    # obtém o valor específico
    wanted_value = cli.get_wanted_value(field)

    return utils.search_by_field(data, field, wanted_value)


def sort_by_field(data: People, field: str, reverse_order: bool) -> People:

    people_list = sorted(
        data,
        key=itemgetter(field),
        reverse=reverse_order
    )

    return people_list


def total_number_of_people_registered(data: People) -> int:
    return len(data)


def edit_person(
    data: People,
    person_id: str,
    password: str,
    field: str,
    parameter: str| int,
) -> EditResult:

    person = find_person(data, person_id)

    if person is None:
        return EditResult.ID_NOT_FOUND

    if not authenticate(person, password):
        return EditResult.INCORRECT_PASSWORD

    updated_person = cast(PersonData, {
        **person,
        field: parameter,
    })

    new_data = remove_person_by_id(data, person_id)
    new_data.append(updated_person)

    save_data(new_data)

    return EditResult.EDITED