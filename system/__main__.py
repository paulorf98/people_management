from system import garantir_pasta
from rich import print
from system import ui
from system import (
    anexar_arquivo,
    listar_pessoas,
    remover_alguem,
    search_by_field,
    sort_by_field,
    all_people_function,
    edit_registration
)


def main():
    garantir_pasta()

    while True:

        choice = ui.main_panel()

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
                    ui.show_removal(nome)
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
                    ui.mostrar_pessoas(mensagem)
                else:
                    ui.mostrar_erro(mensagem)

            case "7":
                people = all_people_function()

                if people == 0:
                    ui.mostrar_erro('Nenhuma pessoa cadastrada')
                else:
                    print(f'há um total de {people} pessoas cadastradas')

            case "8":
                sucesso, mensagem = edit_registration()

                if sucesso:
                    print(mensagem)
                else:
                    ui.mostrar_erro(mensagem)

            case _:
                ui.mostrar_erro("Digite uma opção adequada.")

if __name__ == '__main__':
    main()