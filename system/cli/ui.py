from rich.table import Table
from rich.panel import Panel
from rich import print
from system import Pessoas

def mostrar_pessoas(dados: Pessoas | str, id_completo: bool = False):
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

def show_removal(nome) -> None:
    print(
        Panel(
            f'[green]{nome}[/]',
            title='Sucesso'
        )
    )

def mostrar_erro(texto) -> None:
    print(Panel(f'[yellow]Erro![/] {texto}'))

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


def two_step_verification(text: str) -> str:
    choice = input(f'{text}?\nDigite aqui: ').strip().lower()
    return choice