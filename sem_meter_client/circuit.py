"""Class for the circuit info."""
import json
from typing import TypedDict


class Circuit(TypedDict):
    """Circuit info."""

    id: int
    circuit_alias: str
    number: int
    online: int
    online_on: int
    online_off: int
    type_id: str
    multiplier: str
    typeName: str
    typeImage: str
    electric: str


class CircuitResponse:
    """Class for the circuit response."""

    def __init__(self, json_data: dict) -> None:
        """Initialize the CircuitResponse object."""
        self.code = json_data["code"]
        self.msg = json_data["msg"]
        self.value = [Circuit(**item) for item in json_data["value"]]

    @staticmethod
    def read_circuit_response(response_text: str) -> "CircuitResponse":
        """Read JSON response and return a CircuitResponse object."""
        data = json.loads(response_text)
        return CircuitResponse(data)
