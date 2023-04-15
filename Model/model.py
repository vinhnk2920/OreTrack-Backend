from peewee import *
from Model.base import BaseModel


class User(BaseModel):
    id = IntegerField()
    username = CharField()
    email = CharField()
    password = CharField()
    fullname = CharField()
    dob = DateField()
    phone = CharField()
    avatar = CharField()
    department_id = IntegerField()
    position_id = IntegerField()
    role_id = IntegerField()
    created_at = DateTimeField()
    updated_at = DateTimeField()

    class Meta:
        table_name = "users"


class Disaster(BaseModel):
    id = IntegerField()
    name = CharField()
    address_id = IntegerField()
    risk_level = IntegerField()
    start_at = DateTimeField()
    end_at = DateTimeField()
    created_at = DateTimeField()
    updated_by = IntegerField()

    class Meta:
        table_name = "disasters"


class Addresses(BaseModel):
    id = IntegerField()
    name = CharField()
    parent_id = IntegerField()
    province_id = IntegerField()
    province_name = CharField()
    district_id = IntegerField()
    district_name = CharField()
    street_id = IntegerField()
    street_name = CharField()
    hamlet_id = IntegerField()
    hamlet_name = CharField()
    corner_id = IntegerField()
    corner_name = CharField()
    full_address = CharField()
    lat = FloatField()
    lng = FloatField()
    status = IntegerField()
    created_at = DateTimeField()

    class Meta:
        table_name = "addresses"


class Rescue(BaseModel):
    id = IntegerField()
    disaster_id = IntegerField()
    sos_id = IntegerField()
    department_id = IntegerField()
    status = IntegerField()
    created_at = DateTimeField()
    updated_at = DateTimeField()

    class Meta:
        table_name = "rescue"


class Forecast(BaseModel):
    id = IntegerField()
    name = CharField()
    full_address = CharField()
    disaster_type = IntegerField()
    forecast_start = DateField()
    forecast_end = DateField()
    reported_by = CharField()

    class Meta:
        table_name = "forecasts"


class DisasterType(BaseModel):
    id = IntegerField()
    name = CharField()
    description = CharField()
    image = CharField()
    created_at = DateTimeField()

    class Meta:
        table_name = "disaster_type"


class AlertMessage(BaseModel):
    id = IntegerField()
    name = CharField()
    disaster_id = IntegerField()
    content = CharField()
    created_at = DateTimeField()
    updated_at = DateTimeField()
    created_by = IntegerField()
    updated_by = IntegerField()

    class Meta:
        table_name = "alert_messages"
