
def email_exists(data , email: str) -> bool:
    """
    Verifica se um email já foi cadastrado no banco de dados
    :param data: Banco de dados
    :param email: Verifica se esse email já está cadastrado.
    :return: Retorna True ou False
    """
    return any(person['email'] == email for person in data)