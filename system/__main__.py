from system.database.storage import garantir_pasta
from rich import print as rprint
import system.ui as ui
from system.database.services import (
    anexar_arquivo,
    listar_pessoas,
    remover_alguem,
)


def main():
    garantir_pasta()
    rprint('\n---Sistema de cadastro---')

    while True:

        rprint('''
[bold magenta][1][/]: Novo cadastro
[bold magenta][2][/]: Listar pessoas
[bold magenta][3][/]: Remover alguém
[bold magenta][0][/]: Para sair''')

        escolha = input('\nDigite aqui: ')

        if escolha == '0':
            break

        elif escolha == '1':
            anexar_arquivo()

        elif escolha == '2':
            sucesso, mensagem = listar_pessoas()

            if sucesso:
                ui.mostrar_pessoas(mensagem)
            else:
                ui.mostrar_erro(mensagem)

        elif escolha == '3':
            id_procurado = input('Digite o id: ')
            sucesso, nome = remover_alguem(id_procurado)

            if sucesso:
                ui.mostrar_remocao(nome)
            else:
                ui.mostrar_erro(nome)

        else:
            ui.mostrar_erro('Digite uma opção adequada.')
            continue


if __name__ == '__main__':
    main()