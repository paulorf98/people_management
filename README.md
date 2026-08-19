# 🧾 Sistema de Cadastro em Python
Projeto simples de CRUD com persistência de dados em arquivo JSON.

## Funcionalidades
- Criar pessoa
- Listar pessoas
- Remover pessoa por ID
- Buscar por nome
- Buscar por idade
- Listar por campo e ordem
- Total de pessoas cadastradas
- Editar cadastro

## Tecnologias / Bibliotecas
- Python
- JSON — persistência de dados
- Rich — interface no terminal (CLI)
- email-validator — validação de endereços de e-mail

## Estrutura do projeto

```text
people_management/
├── .gitignore
├── README.md
├── requirements.txt
└── system/
    ├── cli/
    │   ├── ui.py
    │   └── messages.py
    ├── database/
    │   └── storage.py
    ├── models/
    │   └── pessoa.py
    ├── services/
    │   └── people_service.py
    ├── type_aliases.py
    └── main.py
```

## Instalação de dependências
```bash
pip install -r requirements.txt
```

## Como executar

Na raiz do projeto:
### 🪟 Windows
```bash
python -m system
```

### 🐧Linux:
```bash
python3 -m system
```