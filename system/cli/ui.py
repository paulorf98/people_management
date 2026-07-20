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

def mostrar_remocao(nome) -> None:
    print(
        Panel(
            f'[green]{nome}[/] removido com sucesso!',
            title='Sucesso'
        )
    )

def mostrar_erro(texto) -> None:
    print(Panel(f'[yellow]Erro![/] {texto}'))