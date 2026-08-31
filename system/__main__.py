from system import panel, main_panel
from .services.people_services import register, registered_people, delete_person

def main():

    while True:

        choice = main_panel()

        match choice:
            case "0":
                break

            case "1":
                register()

            case "2":
                registered_people()

            case "3":
                delete_person()

            case "4":
                print('Em breve')

            case "5":
                print('Em breve')

            case "6":
                print('Em breve')

            case "7":
                print('Em breve')

            case "8":
                print('Em breve')

            case _:
                panel(category='erro', text='Digite uma opção adequada.')

if __name__ == '__main__':
    main()