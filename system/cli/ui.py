from rich.table import Table
from rich.panel import Panel
from rich import print
from system import Pessoas


def mostrar_pessoas(dados: Pessoas | str, id_completo: bool = False) -> None:
    """
    Cria uma tabela que exibirá dados.

    :param dados: Informações a exibir em tabela
    :param id_completo: True: exibirá id completo. False: Exibirá os 8 primeiros dígitos
    """
    tabela = Table(title='Pessoas cadastradas', title_style='bold magenta')

    tabela.add_column('ID')
    tabela.add_column('Nome')
    tabela.add_column('Idade')

    for pessoa in dados:
        id_exibicao = pessoa['id']

        if not id_completo:
            id_exibicao = id_exibicao[:8] + "..."

        tabela.add_row(
            id_exibicao,
            pessoa["nome"],
            str(pessoa["idade"])
        )

    print(tabela)

def panel(text: str) -> None:
    """
    Recebe um texto para exibir em forma de tabela.

    :param text: Texto a ser exibido na tabela
    """

    print(
        Panel(
            f'[green]{text}[/]',
            title="Sucesso"
        )
    )

def show_result(text: str, type_of_result: str) -> None:
    """
    Recebe um texto para exibir ao usuário, seja em forma de erro ou não conforme o type_of_result.

    :param text: Texto que deseja imprimir ao usuário, sendo ele de erro ou não.
    :param type_of_result: Define se irá imprimir como erro ou não.
    Se for "success" apenas irá exibir o texto. Caso seja "error", exibirá de forma mais explícita.
    """

    if type_of_result == "error":
        print(Panel(f"[red]Erro![/] {text}"))
        return

    if type_of_result == "success":
        print(Panel(f"[green]Success![/] {text}"))
        return

    raise ValueError(f"Tipo de resultado inválido: {type_of_result!r}")


def main_panel() -> str:
    print('\n---Sistema de cadastro---')

    print('''
    [bold magenta][1][/]: Novo cadastro
    [bold magenta][2][/]: Listar pessoas
    [bold magenta][3][/]: Remover alguém
    [bold magenta][4][/]: Buscar usuário por nome/ver ID completo
    [bold magenta][5][/]: Buscar usuário por idade/ver ID completo
    [bold magenta][6][/]: Listar em ordem por campo
    [bold magenta][7][/]: Total de pessoas cadastradas
    [bold magenta][8][/]: Editar cadastro
    [bold magenta][0][/]: Para sair\n''')

    choice = input('Digite aqui: ')
    return choice

def empty_data() -> None:
    show_result("Nenhuma pessoa cadastrada", "error")