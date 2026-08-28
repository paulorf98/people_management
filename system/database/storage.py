import json

def load_data():
    try:
        with open('system/people.json', 'r', encoding='utf-8') as archive:
            return json.load(archive)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data(data) -> None:
    with open('system/people.json', 'w', encoding='utf-8') as archive:
        json.dump(data, archive, ensure_ascii=False, indent=4)