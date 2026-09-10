from system.cli import client as cli


def main() -> None:

    while True:

        choice = cli.main_panel()

        match choice:
            case "0":
                break

            case "1":
                cli.register_flow()

            case "2":
                cli.registered_people_flow()

            case "3":
                cli.delete_person_flow()

            case "4":
                cli.search_people_flow()

            case "5":
                cli.sort_by_field_flow()

            case "6":
                cli.total_number_of_people_flow()

            case "7":
                cli.edit_person_flow()

            case _:
                cli.panel(category='erro', text='Digite uma opção adequada.')

if __name__ == '__main__':
    main()