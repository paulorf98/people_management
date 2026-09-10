from typing import cast
from uuid import uuid4

from system.database.storage import save_data
from system.models.person import Person
from system.services.results import EditResult
from system.type_aliases import People, PersonData
from system.utils import people_utils as utils
from system.utils.people_utils import find_person, remove_person_by_id
from system.utils.validation import EditableFields, authenticate


def create_person(name: str, age: int, email: str, password: str) -> Person:
 # Cria a pessoa em formato dataclass
    return Person(
        id=str(uuid4()),
        name=name,
        age=age,
        email=email,
        password=password
    )


def register(data: People, person: Person) -> bool:

    # Torna compatível com JSON
    person_data: PersonData = person.to_dict()

    # Verifica se o email já existe
    exists = utils.email_exists(data=data, email=person_data['email'])
    if exists:
        return False

    # Adiciona a nova pessoa
    data.append(person_data)

    # Reescreve o JSON e salva o arquivo
    save_data(data)

    # Retorna que foi um sucesso
    return True


def delete_person(
    data: People,
    person: PersonData,
    password: str,
) -> bool:

    if not authenticate(person, password):
        return False

    new_data = remove_person_by_id(data, person["id"])
    save_data(new_data)

    return True


def edit_person(
    data: People,
    person_id: str,
    password: str,
    field: EditableFields,
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