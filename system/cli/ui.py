from rich.table import Table
from rich.panel import Panel
from rich import print

from system.type_aliases import People
from system.utils import validation as valid
from system.services import people_services as services


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
    [bold magenta][nome] [/]: Alterar o nome
    [bold magenta][idade][/]: Alterar a idade
    [bold magenta][email][/]: Alterar o email
    [bold magenta][senha][/]: Alterar a senha
    [bold magenta]0[/]: Voltar\n''')

    choice: str = input('Digite aqui: ').strip().lower()
    return choice


def show_people(data, full_id: bool = False) -> None:
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
        "INCORRECT_PASSWORD": "Senha inválida ou muito fraca.",
        "LIMIT_OF_ATTEMPTS": "Limite de tentativas excedido.",
        "EMAIL_EXISTS": "Este email já existe.",
    },
    "sucesso": {
        "USER_CREATED": "Usuário criado com sucesso!",
        "PERSON_REMOVED": "Pessoa removida com sucesso!"
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
    while True:
        try:
            return valid.validate_password(input('Digite uma senha: '))
        except ValueError as error:
            panel(category='erro', text=str(error))

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

        panel("erro", text="Digite um campo válido")


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


def search_people_flow() -> None:
    success: People | None = services.search_people()

    if not success:
        panel("info", key="USER_NOT_FOUND")
        return

    show_people(success)
