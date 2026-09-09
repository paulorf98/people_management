from rich import print
from rich.panel import Panel
from rich.table import Table

from system.database.storage import load_data
from system.services import people_services as services
from system.services.results import EditResult
from system.type_aliases import People, PersonData
from system.utils import validation as valid
from system.utils.people_utils import find_person, search_by_field, sort_by_field


# Painel principal
def main_panel() -> str:
    print('\n---Sistema de cadastro---')

    print('''
    [bold magenta][1][/]: Novo cadastro
    [bold magenta][2][/]: Listar pessoas
    [bold magenta][3][/]: Remover alguém
    [bold magenta][4][/]: Buscar usuário por campo
    [bold magenta][5][/]: Listar em ordem por campo
    [bold magenta][6][/]: Total de pessoas cadastradas
    [bold magenta][7][/]: Editar cadastro
    [bold magenta][0][/]: Para sair\n''')

    choice: str = input('Digite aqui: ')
    return choice


# Painel de edição de cadastro
def edit_panel() -> str:
    print('\n---Editar Cadastro---')

    print('''
    [bold magenta][1][/]: Alterar o nome
    [bold magenta][2][/]: Alterar a idade
    [bold magenta][3][/]: Alterar o email
    [bold magenta][4][/]: Alterar a senha
    [bold magenta][5][/]: Voltar\n''')

    choice: str = input('Digite aqui: ').strip().lower()
    return choice


def get_parameter(field: str) -> str | int:
    if field == "name":
        return ask_name()
    elif field == "age":
        return ask_age()
    elif field == "email":
        return ask_email()
    elif field == "password":
        return ask_password()
    
    raise ValueError(f"Campo editável inválido: {field!r}")


def show_people(data: People, full_id: bool = False) -> None:
    """
    Cria uma tabela que exibirá dados.

    :param data: Informações a exibir em tabela
    :param full_id: True: exibirá id completo. False: Exibirá os 8 primeiros dígitos
    """
    tabela = Table(title='Pessoas cadastradas', title_style='bold magenta')

    # Adiciona as colunas da tabela
    tabela.add_column('ID')
    tabela.add_column('Nome')
    tabela.add_column('Idade')
    tabela.add_column('Email')

    # Adiciona as informações de cada pessoa na tabela
    for person in data:
        id_exibicao = person['id']

        if not full_id:
            id_exibicao = id_exibicao[:8] + "..."

        tabela.add_row(
            id_exibicao,
            person["name"],
            str(person["age"]),
            person["email"])
    print(tabela)


# Mensagens do sistema ao usuário
MESSAGES = {
    "info": {
        "USER_NOT_FOUND": "Usuário não encontrado.",
        "ID_NOT_FOUND": "ID não encontrado.",
        "EMPTY_DATA": "Nenhuma pessoa cadastrada.",
    },
    "erro": {
        "INVALID_VALUE": "O Valor é inválido.",
        "INCORRECT_PASSWORD": "Senha inválida.",
        "LIMIT_OF_ATTEMPTS": "Limite de tentativas excedido.",
        "EMAIL_EXISTS": "Este email já existe.",
    },
    "sucesso": {
        "USER_CREATED": "Usuário criado com sucesso!",
        "PERSON_REMOVED": "Pessoa removida com sucesso!",
        "EDITED_PERSON": "Usuário editado com sucesso!"
    }
}


def panel(category: str, key: str | None = None, text: str | None = None) -> None:
    styles = {
        "erro": ("red", "Erro!"),
        "sucesso": ("green", "Sucesso!"),
        "info": ("blue", "Info:"),
    }

    if category not in styles:
        raise ValueError(f"Categoria inválida: {category!r}")

    # 1. Pega a mensagem baseada na prioridade (key primeiro, depois text)
    if key is not None:
        category_messages = MESSAGES.get(category, {})
        if key not in category_messages:
            raise KeyError(f"Chave {key!r} não encontrada na categoria {category!r}")
        content = category_messages[key]
    elif text is not None:
        content = text
    else:
        raise ValueError("Você deve fornecer 'key' ou 'text'.")

    # 2. Renderiza o painel
    color, prefix = styles[category]
    print(Panel(f"[{color}]{prefix}[/] {content}"))


def ask_name() -> str:
    while True:
        try:
            return valid.validate_name(input('Digite o seu nome: '))
        except ValueError as error:
            panel(category='erro', text=str(error))


def ask_age() -> int:
    while True:
        try:
            return valid.validate_age(input('Digite a sua idade: '))
        except ValueError as error:
            panel(category='erro', text=str(error))


def ask_email() -> str:
    while True:
        try:
            return valid.validate_email_address(input('Digite o seu email: '))
        except ValueError as error:
            panel(category='erro', text=str(error))


def ask_password() -> str:
    """
    Força o usuário a digitar uma senha válida. Ideal para cadastrar uma senha ou alterá-la.

    :return: Retorna a senha
    """
    while True:
        try:
            return valid.validate_password(input('Digite uma senha: '))
        except ValueError as error:
            panel(category='erro', text=str(error))


def get_password() -> str:
    """
    Pergunta qual a senha do usuário. Ideal para quando o usuário precisa usar sua senha sem a alterar.

    :return: Retorna a senha informada pelo usuário.
    """
    return input("Digite sua senha: ")


def get_person_id() -> str:
    return input('Digite o seu id: ')


def confirm(text: str) -> bool:
    while True:
        _confirm = input(text).strip().upper()

        if _confirm == "S":
            return True

        elif _confirm == "N":
            return False

        else:
            print("Digite apenas S ou N.")


# obter campo válido
def get_valid_field() -> valid.SearchableField:
    """
    Administra a interação com o usuário até obter um campo válido pelo usuário.

    :return: SearchableField (campo válido para pesquisa)
    """
    while True:
        field = input("Digite o campo (id, name, age, email): ")

        if valid.validate_field(field):
            return field

        panel("erro", key="INVALID_VALUE")


# obter campo válido
def get_valid_editable_field() -> valid.EditableFields:
    """
     Administra a interação com o usuário até obter um campo válido pelo usuário.

    :return: EditableFields (campo válido para edição do cadastro)
    """
    while True:
        field = input("Digite o campo (name, age, email, password): ")

        if valid.validate_editable_fields(field):
            return field

        panel("erro", key="INVALID_VALUE")


# obter um parâmetro
def get_wanted_value(field: valid.SearchableField) -> str | int:
    """
    Administra a interação com o usuário para obter o valor desejado.
    Ex.: name="Paulo", age=18 etc

    :return: str
    """

    if field == "name":
        return input("Nome da pessoa: ")

    elif field == "age":
        while True:
            try:
                return int(input("Idade da pessoa: "))
            except ValueError:
                panel("erro", text="Digite apenas números em idade.")

    return input(f"{field.capitalize()} da pessoa: ")

def get_reverse_order() -> bool:
    while True:
        reverse: str = input("Deseja ver em ordem reversa? (S/N): ").strip().upper()

        if reverse == "S":
            return True
        
        elif reverse == "N":
            return False
        
        else:
            panel(category="erro", text="Digite uma opção adequada")
            continue



def register_flow() -> None:
    data: People = load_data()

    name = ask_name()
    age = ask_age()
    email = ask_email()
    password = ask_password()

    person = services.create_person(name, age, email, password)

    result = services.register(data, person)

    if not result:
        panel(category="erro", key="EMAIL_EXISTS")
        return

    panel('sucesso', key='USER_CREATED')
    

def registered_people_flow() -> None:
    data: People = load_data()

    if not data:
        panel("info", key="EMPTY_DATA")
        return
    
    show_people(data)


def delete_person_flow() -> None:
    data: People = load_data()

    person_id = get_person_id()
    password = get_password()

    person: PersonData | None = find_person(data, person_id)
    
    if person is None:
        panel("info", key="ID_NOT_FOUND")
        return

    stop = confirm( f"Deseja mesmo excluir {person['name']}? S/N: " ) 

    if not stop: 
        panel("info", text=f"A remoção de {person['name']} foi cancelada " 
                           f"e o usuário não foi deletado." )
        return

    result = services.delete_person(
        data,
        person,
        password
    )

    if not result:
        panel("erro", key="INCORRECT_PASSWORD")
        return

    panel("sucesso", key="PERSON_REMOVED")


def search_people_flow() ->  None:
    data: People = load_data()

    field: valid.SearchableField = get_valid_field()
    wanted_value: str | int = get_wanted_value(field)

    people: People | None = search_by_field(data, field, wanted_value)

    if people is None:
        panel("info", key="USER_NOT_FOUND")
        return

    show_people(people)


def sort_by_field_flow() -> None:
    data: People = load_data()

    field = get_valid_field()

    reverse_order = get_reverse_order()

    people = sort_by_field(data, field, reverse_order)

    if not people:
        panel("info", key="USER_NOT_FOUND")
        return

    show_people(people, True)


def total_number_of_people_flow() -> None:
    data: People = load_data()

    total = len(data)

    if total == 0:
        panel("info", key="EMPTY_DATA")
        return

    print(f"Há um total de [blue]{total}[/] pessoa(s) cadastradas.")


def edit_person_flow():
    data = load_data()


    person_id = get_person_id()
    password = get_password()


    field = get_valid_editable_field()
    parameter = get_parameter(field)


    result = services.edit_person(data, person_id, password, field, parameter)

    if result == EditResult.ID_NOT_FOUND:
        panel("info", key="ID_NOT_FOUND")

    elif result == EditResult.INCORRECT_PASSWORD:
        panel("erro", key="INCORRECT_PASSWORD")

    else:
        panel("sucesso", key="EDITED_PERSON")