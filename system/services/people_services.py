from system.cli import ui
from system.models.person import Person
from uuid import uuid4
from system.database import load_data, save_data

def create_person_flow() -> Person:
    name = ui.ask_name()
    age = ui.ask_age()
    email = ui.ask_email()
    password = ui.ask_password()

    person = Person(
        id=str(uuid4()),
        name=name,
        age=age,
        email=email,
        password=password
    )

    ui.panel('sucesso', key='USER_CREATED')
    return person

def register() -> None:
    person = create_person_flow()
    person_data = person.to_dict()
    data = load_data()
    data.append(person_data)
    save_data(data)