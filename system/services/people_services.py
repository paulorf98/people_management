from system.cli import ui
from system.models.person import Person
from uuid import uuid4
from system.database import load_data, save_data
from system.type_aliases import PersonData, People
from system.utils import people_utils as utils


def create_person_flow() -> Person:
    # Verifica os dados informados
    name = ui.ask_name()
    age = ui.ask_age()
    email = ui.ask_email()
    password = ui.ask_password()

    # Cria a pessoa em formato dataclass
    person = Person(
        id=str(uuid4()),
        name=name,
        age=age,
        email=email,
        password=password
    )

    return person


def register() -> None:
    # Cria a pessoa
    person: Person = create_person_flow()

    # Torna compatível com JSON
    person_data: PersonData = person.to_dict()

    # Carrega os dados em JSON
    data: People = load_data()

    # Verifica se o email já existe
    exists = utils.email_exists(data=data, email=person_data['email'])
    if exists:
        ui.panel(category="erro", key="EMAIL_EXISTS")
        return

    # Adiciona a nova pessoa
    data.append(person_data)

    # Reescreve o JSON e salva o arquivo
    save_data(data)

    ui.panel('sucesso', key='USER_CREATED')


def registered_people() -> None:
    data: People = load_data()

    # Verifica se a lista está vazia
    if not data:
        ui.panel("info", key="EMPTY_DATA")
        return

    # lista as pessoas em formato de tabela
    ui.show_people(data)

# ADICIONE UMA VERIFICAÇÃO DA SENHA PARA EXCLUIR O USUÁRIO, COMO UM "authenticate(person, password)".
def delete_person() -> None:
    """
    Coordena o fluxo de remoção de uma pessoa.

    Obtém o ID, valida a existência da pessoa,
    solicita confirmação e persiste a remoção.

    :return: None
    """
    data: People = load_data()

    person_id = ui.get_person_id()
    found_person = utils.find_person(data, person_id)

    if found_person is None:
        ui.panel(category="erro", text="Pessoa não encontrada.")
        return

    confirm = ui.confirm(
        f"Deseja mesmo excluir {found_person['name']}? S/N: "
    )

    if not confirm:
        ui.panel(
            "info",
            text=f"A remoção de {found_person['name']} foi cancelada "
                 f"e o usuário não foi deletado."
        )
        return

    updated_data = utils.remove_person_by_id(data, person_id)
    save_data(updated_data)
    ui.panel(category="sucesso", key="PERSON_REMOVED")


def search_people() -> People | None:
    data: People = load_data()

    # Obtém o campo
    field = ui.get_valid_field()

    # obtém o valor específico
    wanted_value = ui.get_wanted_value(field)

    return utils.search_by_field(data, field, wanted_value)