import json

from system.type_aliases import People


def load_data() -> People:
    try:
        with open('system/people.json', 'r', encoding='utf-8') as archive:
            return json.load(archive)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data(data: People) -> None:
    with open('system/people.json', 'w', encoding='utf-8') as archive:
        json.dump(data, archive, ensure_ascii=False, indent=4)