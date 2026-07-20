from system.database import garantir_pasta
from rich import print
from system.cli import ui, mostrar_pessoas
from system.services import (
    anexar_arquivo,
    listar_pessoas,
    remover_alguem,
    search_by_field,
    sort_by_field
)


def main():
    garantir_pasta()
    print('\n---Sistema de cadastro---')

    while True:

        print('''
[bold magenta][1][/]: Novo cadastro
[bold magenta][2][/]: Listar pessoas
[bold magenta][3][/]: Remover alguém
[bold magenta][4][/]: Buscar usuário por nome/ver ID completo
[bold magenta][5][/]: Buscar usuário por idade/ver ID completo
[bold magenta][6][/]: Listar em ordem por campo
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
                sucesso, mensagem = search_by_field('nome')

                if sucesso:
                    ui.mostrar_pessoas(mensagem, True)
                else:
                    ui.mostrar_erro(mensagem)

            case "5":
                sucesso, mensagem = search_by_field('idade')

                if sucesso:
                    ui.mostrar_pessoas(mensagem, True)
                else:
                    ui.mostrar_erro(mensagem)

            case "6":
                field = input('Digite o campo (nome, idade...) para listar em ordem: ').strip().lower()
                reverse = input('Deseja ver em ordem decrescente?\nSe sim digite S:  ').strip().lower()

                if reverse == 's':
                    sucesso, mensagem = sort_by_field(field, True)
                else:
                    sucesso, mensagem = sort_by_field(field)

                if sucesso:
                    mostrar_pessoas(mensagem)
                else:
                    ui.mostrar_erro(mensagem)

            case _:
                ui.mostrar_erro("Digite uma opção adequada.")

if __name__ == '__main__':
    main()