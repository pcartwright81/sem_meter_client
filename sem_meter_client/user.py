"""Define the User class and a function to read JSON into a User object."""

import json
from dataclasses import dataclass


@dataclass
class User:
    """Represents a user object returned from the API."""

    id: str
    email: str
    image: str
    nickname: str
    address: str
    sex: str
    telephone: str
    iphone: str
    token: str

    @staticmethod
    def read_user_response(json_text: str) -> "User":
        """Read JSON text and return a User object."""
        data = json.loads(json_text)
        user_data = data.get("value")
        return User(**user_data)
