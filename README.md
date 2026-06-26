# 🧾 Sistema de Cadastro em Python
Projeto simples de CRUD usando JSON como armazenamento local.

## Funcionalidades
- Criar usuário
- Listar usuários
- Remover usuário por ID

## Tecnologias / Bibliotecas
- Python
- JSON
- Rich (CLI)
- email-validator

## Estrutura do projeto

```md id="fix1"
people_management/
│
├── system/
│   ├── __init__.py
│   ├── main.py
│   ├── ui.py
│   ├── models/
│   │   └── pessoa.py
│   └── database/
│       ├── services.py
│       └── storage.py
│
├── data/
│   └── cadastrados.json
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Instalação de dependências

pip install -r requirements.txt

## Como executar

### 🪟 Windows / Geral
```bash
python -m system
```

### 🐧Linux:
```bash
python3 -m system
```