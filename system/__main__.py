from system.cli import ui

def main():

    while True:

        choice = ui.main_panel()

        match choice:
            case "0":
                break

            case "1":
                ui.register_flow()

            case "2":
                ui.registered_people_flow()

            case "3":
                ui.delete_person_flow()

            case "4":
                ui.search_people_flow()

            case "5":
                ui.sort_by_field_flow()

            case "6":
                ui.total_number_of_people_flow()

            case "7":
                print('Em breve')

            case _:
                ui.panel(category='erro', text='Digite uma opção adequada.')

if __name__ == '__main__':
    main()