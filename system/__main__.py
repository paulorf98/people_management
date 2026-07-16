from system.database import garantir_pasta
from rich import print
from system.cli import ui
from system.services import (
    anexar_arquivo,
    listar_pessoas,
    remover_alguem,
    search_name
)


def main():
    garantir_pasta()
    print('\n---Sistema de cadastro---')

    while True:

        print('''
[bold magenta][1][/]: Novo cadastro
[bold magenta][2][/]: Listar pessoas
[bold magenta][3][/]: Remover alguém
[bold magenta][4][/]: Buscar por nome
[bold magenta][0][/]: Para sair''')

        choice = input("\nDigite aqui: ")

        match choice:
            case "0":
                break

            case "1":
                sucesso, mensagem = anexar_arquivo()

                if sucesso:
                    print(mensagem)
                else:
                    ui.mostrar_erro(mensagem)

            case "2":
                sucesso, mensagem = listar_pessoas()

                if sucesso:
                    ui.mostrar_pessoas(mensagem)
                else:
                    ui.mostrar_erro(mensagem)

            case "3":
                id_procurado = input("Digite o id: ")
                sucesso, nome = remover_alguem(id_procurado)

                if sucesso:
                    ui.mostrar_remocao(nome)
                else:
                    ui.mostrar_erro(nome)

            case "4":
                sucesso, mensagem = search_name()

                if sucesso:
                    # A função mostrar_pessoas() espera receber uma lista de dicionários.
                    # Como search_name() retorna apenas um dicionário (uma única pessoa),
                    # esse dicionário estará numa lista para manter o formato esperado
                    ui.mostrar_pessoas([mensagem])
                else:
                    ui.mostrar_erro(mensagem)

            case _:
                ui.mostrar_erro("Digite uma opção adequada.")

if __name__ == '__main__':
    main()