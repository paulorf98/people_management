from system import register, panel, main_panel

def main():

    while True:

        choice = main_panel()

        match choice:
            case "0":
                break

            case "1":
                register()

            case "2":
                print('Em breve')

            case "3":
                print('Em breve')

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