from email_validator import validate_email, EmailNotValidError


def validate_name(name: str) -> str:
    name = name.strip().title()
    if not name or not all(p.isalpha() for p in name.split()):
        raise ValueError("Nome deve conter apenas letras e espaços.")
    return name


def validate_age(raw_age: str | int) -> int:
    try:
        age = int(raw_age)
    except ValueError:
        raise ValueError("A idade deve ser um número inteiro.")
    if not (0 < age <= 122):
        raise ValueError("A idade deve estar entre 1 e 122 anos.")
    return age


def validate_password(password: str) -> str:
    has_min = len(password) >= 8
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$" for c in password)

    if not all([has_min, has_upper, has_digit, has_special]):
        raise ValueError("Senha fraca (requer 8+ caracteres, maiúscula, número e símbolo).")
    return password


def validate_email_address(email: str) -> str:
    try:
        return validate_email(email.strip()).normalized
    except EmailNotValidError as e:
        raise ValueError(f"E-mail inválido: {e}")


