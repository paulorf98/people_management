import json
from typing import cast

from system.type_aliases import People


def load_data() -> People:
    try:
        with open('system/people.json', 'r', encoding='utf-8') as archive:
            data = json.load(archive)
            return cast(People, data)
    except (FileNotFoundError, json.JSONDecodeError):
        empty_list: People = []
        return empty_list

    
def save_data(data: People) -> None:
    with open('system/people.json', 'w', encoding='utf-8') as archive:
        json.dump(data, archive, ensure_ascii=False, indent=4)