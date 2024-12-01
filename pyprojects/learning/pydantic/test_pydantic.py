from datetime import date
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    birthday_date: date


user_name = User(id=1,
                 name="Nikita",
                 birthday_date=date(year=1998, month=3, day=26))

to_dict = user_name.model_dump()
to_json = user_name.model_dump_json()

print(to_dict, type(to_dict))
print(to_json, type(to_json))

alex = User(id="2",
            name='Алексей',
            birthday_date="1990-11-22")

to_dict = alex.model_dump()
to_json = alex.model_dump_json()

print(to_dict, type(to_dict))
print(to_json, type(to_json))

dima = User(id="3",
            name=156,
            birthday_date="1990-11-22")

to_dict = dima.model_dump()
to_json = dima.model_dump_json()

print(to_dict, type(to_dict))
print(to_json, type(to_json))