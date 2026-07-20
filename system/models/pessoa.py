from email_validator import validate_email, EmailNotValidError
from rich import print
from uuid import uuid4


def verificar_nome() -> str:
    while True:
        name = input('Digite seu nome: ').strip()
        if name and all(part.isalpha() for part in name.split()):
            return name
        print('[yellow]Nome inválido![/] Use apenas letras e espaços.')


def verificar_idade() -> int:
    while True:
        try:
            idade = int(input('Digite sua idade: '))
            if 0 < idade <= 122:
                return idade
            print('Idade [yellow]inválida![/] Digite uma idade entre 1 e 122.')
        except ValueError:
            print('[red]Somente números são permitidos![/]')


def verificar_email() -> str:
    while True:
        try:
            email = input('Digite o seu email: ').strip()
            email_valido = validate_email(email)
            email_final = email_valido.normalized
            return email_final
        except EmailNotValidError as e:
            print(f"Email [yellow]inválido![/] Motivo: [blue]{e}.[/] Tente novamente.")


def criar_nova_senha() -> str:
    while True:
        senha = input('Digite sua senha: ')

        if len(senha) >= 5:
            return senha

        print('Sua senha deve conter no mínimo [red]5[/] caracteres.')


def cadastrar():
    print('\n---Iniciando cadastro---')
    name = verificar_nome()
    age = verificar_idade()
    email = verificar_email()
    password = criar_nova_senha()
    print('---Cadastro finalizado---')

    return {
        'id': str(uuid4()),
        'nome': name,
        'idade': age,
        'email': email,
        'senha': password
    }