from system.models.pessoa import cadastrar
from system.database.storage import (
    carregar_dados,
    salvar_dados
)


def anexar_arquivo():
    nova_pessoa = cadastrar()

    dados = carregar_dados()

    if any(p["email"] == nova_pessoa["email"] for p in dados):
        return False, "Este email já está cadastrado."

    dados.append(nova_pessoa)
    salvar_dados(dados)

    return True, "Cadastro realizado com sucesso!"


def listar_pessoas():
    dados = carregar_dados()

    if not dados:
        return False, 'Nenhuma pessoa cadastrada'

    return True, dados


def remover_alguem(id_procurado):
    dados = carregar_dados()

    if not dados:
        return False, 'Nenhuma pessoa cadastrada.'

    nova_lista = []
    nome_removido = None

    for pessoa in dados:
        if pessoa['id'] == id_procurado:
            nome_removido = pessoa['nome']
            continue
        nova_lista.append(pessoa)

    if nome_removido is None:
        return False, 'ID não encontrado.'

    salvar_dados(nova_lista)
    return True, nome_removido