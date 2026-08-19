from system import garantir_pasta
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
                anexar_arquivo()

            case "2":
                listar_pessoas()

            case "3":
                remover_alguem()

            case "4":
                search_by_field("nome")

            case "5":
                search_by_field("idade")

            case "6":
                sort_by_field()

            case "7":
                all_people_function()

            case "8":
                edit_registration()

            case _:
                ui.show_result("Digite uma opção adequada.", "error")

if __name__ == '__main__':
    main()