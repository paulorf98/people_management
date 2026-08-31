from system.type_aliases import People, PersonData
from .validation import SearchableField

def email_exists(data: People, email: str) -> bool:
    """
    Verifica se um email já foi cadastrado no banco de dados
    :param data: Banco de dados
    :param email: Verifica se esse email já está cadastrado.
    :return: Retorna True ou False
    """
    return any(person['email'] == email for person in data)


def find_person(data: People, person_id: str) -> PersonData | None:
    """Retorna a pessoa cujo id informado seja igual ao id da pessoa cadastrada"""
    for person in data:
        if person['id'] == person_id:
            return person

    return None

def remove_person_by_id(data: People, person_id: str) -> People:
    """Retorna uma nova lista sem a pessoa do ID informado."""
    return [person for person in data if person['id'] != person_id]


def search_by_field(data: People, field: SearchableField, wanted_value: str) -> People | None:
    """
    Retorna uma lista com as pessoas encontradas.
    """
    found_users: People = []

    for person in data:
        if person[field] == wanted_value:
            found_users.append(person)

    if found_users is None:
        return None

    return found_users