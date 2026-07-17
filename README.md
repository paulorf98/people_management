# 🧾 Sistema de Cadastro em Python
Projeto simples de CRUD usando JSON como armazenamento local.

## Funcionalidades
- Criar usuário
- Listar usuários
- Remover usuário por ID
- Buscar por nome
- busca por idade

## Tecnologias / Bibliotecas
- Python
- JSON
- Rich (CLI)
- email-validator

## Estrutura do projeto

```md id="fix1"
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
    └── main.py
```

## Instalação de dependências

pip install -r requirements.txt

## Como executar

### 🪟 Windows
```bash
python -m system
```

### 🐧Linux:
```bash
python3 -m system
```