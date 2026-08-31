from dataclasses import dataclass
from system.type_aliases import PersonData
from system.utils.validation import (
    validate_name,
    validate_age,
    validate_password,
    validate_email_address
)

@dataclass
class Person:
    id: str
    name: str
    age: int
    email: str
    password: str

    def __post_init__(self):
        self.name = validate_name(self.name)
        self.age = validate_age(self.age)
        self.email = validate_email_address(self.email)
        self.password = validate_password(self.password)

    def to_dict(self) -> PersonData:
        """Converte a instância de Person para dicionário."""
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "password": self.password,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Person":
        """Cria uma instância de Person a partir de um dicionário."""
        return cls(
            id=data["id"],
            name=data["name"],
            age=int(data["age"]),
            email=data["email"],
            password=data["password"],
        )