import json


class EquipmentList:
    def __init__(self, json_data):
        self.code = json_data["code"]
        self.msg = json_data["msg"]
        self.value = [Equipment(**item) for item in json_data["value"]]

    @staticmethod
    def read_equipment_response(response_text: str) -> "EquipmentList":
        data = json.loads(response_text)
        return EquipmentList(data)


class Equipment:
    def __init__(self, **kwargs):
        self.facility_id = kwargs.get("facility_id")
        self.facility_number = kwargs.get("facility_number")
        self.facility_alias = kwargs.get("facility_alias")
        self.online_on = kwargs.get("online_on")
        self.online_off = kwargs.get("online_off")
        self.versions = kwargs.get("versions")
        self.online = kwargs.get("online")
        self.family = Family(**kwargs.get("family", {}))
        self.notification = Notification(**kwargs.get("notification", {}))
        self.home_name = kwargs.get("home_name")
        self.pitch = kwargs.get("pitch")


class Family:
    def __init__(self, **kwargs):
        self.id = kwargs.get("id")
        self.facility_id = kwargs.get("facility_id")
        self.home_name = kwargs.get("home_name")
        self.address = kwargs.get("address")
        self.price = kwargs.get("price")
        self.billingtime = kwargs.get("billingtime")
        self.etc = kwargs.get("etc")
        self.utc = kwargs.get("utc")
        self.time_name = kwargs.get("time_name")
        self.facility_alias = kwargs.get("facility_alias")


class Notification:
    def __init__(self, **kwargs):
        self.online_on = kwargs.get("online_on")
        self.online_off = kwargs.get("online_off")
