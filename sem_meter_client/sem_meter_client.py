"""Client for the SEM Meter API."""


import aiohttp

from .circuit import CircuitList
from .equipment import EquipmentList
from .user import User


class SEMMeterClient:
    """Client for the SEM Meter API."""

    _base_url = "https://sem-meter.tumblevd.com/index"
    _fcm_token = "cn0IPHVGS3qrJdp5SRHqGy:APA91bFrEGN3Mca9oB9FLhDzrKbCqZ-rzts4oAqVYcEtFkYh6O9vLMg63juL6cI7y7VqT00B5O93NmqRBSbYi5eMLXCRVUx-Bzu8C65Z-rRQQ2kLa2JNpdE"  # noqa: E501, S105

    current_token: str | None = None

    async def login(self, username: str, password: str, timezone: str) -> User:
        """Login to the SEM Meter API."""
        url = f"{self._base_url}/Login/login"
        data = {
            "identificationCode": "1",
            "password": password,
            "phone_type": 0,
            "login_type": 1,
            "fcmToken": self._fcm_token,
            "email": username,
            "gmt": timezone,
        }
        async with (
            aiohttp.ClientSession() as session,
            session.post(url, data=data) as response,
        ):
            response_text = await response.text()
            return User.read_user_response(response_text)

    async def get_equipment_list(self) -> EquipmentList:
        data = {"token": self.current_token}
        url = f"{self._base_url}/Equipment/EquipmentsList"
        async with (
            aiohttp.ClientSession() as session,
            session.post(url, data=data) as response,
        ):
            response_text = await response.text()
            return EquipmentList.read_equipment_response(response_text)

    async def get_circuit_list(self, facility_id: str) -> CircuitList:
        data = {"token": self.current_token, "facility_id": facility_id}
        url = f"{self._base_url}/circuit/list"
        async with (
            aiohttp.ClientSession() as session,
            session.post(url, data=data) as response,
        ):
            response_text = await response.text()
            return CircuitList.read_circuit_response(response_text)
