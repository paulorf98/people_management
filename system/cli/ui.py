from rich.table import Table
from rich.panel import Panel
from rich import print

def mostrar_pessoas(dados):
    tabela = Table(title='Pessoas cadastradas', title_style='bold magenta')

    tabela.add_column('ID')
    tabela.add_column('Nome')
    tabela.add_column('Idade')

    for pessoa in dados:

        id_exibicao = pessoa.get('id')

        if id_exibicao:
            id_exibicao = id_exibicao[:8] + '...'
        else:
            id_exibicao = 'N/A'

        tabela.add_row(
            id_exibicao,
            pessoa.get('nome', 'N/A'),
            str(pessoa.get('idade', 'N/A'))
        )

    print(tabela)

def mostrar_remocao(nome):
    print(
        Panel(
            f'[green]{nome}[/] removido com sucesso!',
            title='Sucesso'
        )
    )

def mostrar_erro(texto):
    print(Panel(f'[yellow]Erro![/] {texto}'))