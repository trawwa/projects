from pydantic import BaseModel, field_validator, model_validator, computed_field, Field, ConfigDict
from datetime import date
from dateutil.relativedelta import relativedelta
from uuid import uuid4
from typing_extensions import Annotated


class User(BaseModel):
    id: Annotated[
        int,
        Field(
        default=1,
        description="Уникальный идентификатор пользователя",
        gt = 0
        )]
    name: Annotated[
        str,
        Field(
        min_length=3,
        max_length=20,
        default="John Doe",
        title="Имя пользователя",
        description="Полное имя"
        )]
    email: Annotated[
        str,
        Field(
        pattern=r"[^@]+@[^@]+\.[^@]+",
        description="Электронная почта должна быть в корректном формате"
        )]
    role: Annotated[
        str,
        Field(
        default="user",
        alias="user_role",
        description="Роль пользователя в системе"
        )]
    phone_number: str = Field(
        pattern=r"^\+\d{1,3}\s?\d{4,14}$",
        description="Номер телефона должен быть в формате +123456789"
        )
    username: str = Field(
        alias="user_name"
        )
    password: str = Field(
        exclude=True
        )
    

class Product(BaseModel):
    price: float = Field(
        gt=0,
        description="Цена должна быть больше нуля"
        )
    name: str = Field(
        min_length=2,
        max_length=50,
        description="Название продукта должно быть от 2 до 50 символов"
        )
    rating: int = Field(
        ge=1,
        le=5,
        description="Рейтинг должен быть от 1 до 5")
    

class Item(BaseModel):
    id: str = Field(
        default_factory=lambda: uuid4().hex
        )
    

class Config(BaseModel):
    debug_mode: bool = Field(repr=False)


class MyModel(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
        )



# Drafts

# user_name = User(id=1,
#                  name="Nikita",
#                  birthday_date=date(year=1998, month=3, day=26))

# to_dict = user_name.model_dump()
# to_json = user_name.model_dump_json()

# print(to_dict, type(to_dict))
# print(to_json, type(to_json))

# alex = User(id="2",
#             name='Алексей',
#             birthday_date="1990-11-22")

# to_dict = alex.model_dump()
# to_json = alex.model_dump_json()

# print(to_dict, type(to_dict))
# print(to_json, type(to_json))

# dima = User(
#     id="3",
#     name=("Коля", True, False, 0, 19933),
#     birthday_date="1990-11-22"
# )

# to_dict = dima.model_dump()
# to_json = dima.model_dump_json()

# print(to_dict, type(to_dict))
# print(to_json, type(to_json)) 

#     @field_validator('name', mode='before')
#     def validate_name(cls, v):
#         if isinstance(v, int):
#             return str(v)
#         elif isinstance(v, str):
#             return v
#         else:
#             raise ValueError("Имя должно быть строкой или числом")

#     @model_validator(mode='after')
#     def check_age(self):
#         today = date.today()
#         age = today.year - self.birthday_date.year - (
#             (today.month, today.day) < (self.birthday_date.month, self.birthday_date.day))

#         if age < 18:
#             raise ValueError("Пользователь должен быть старше 18 лет")
#         if age > 120:
#             raise ValueError("Возраст не может превышать 120 лет")
#         return self

#     @model_validator(mode='after')
#     def set_default_name(self):
#         if self.name.strip() == '':
#             self.name = f"User_{self.id}"
#         return self  


# try:
#     user = User(id=1, name="John", birthday_date=date(2000, 1, 1))
#     print(user)
# except ValueError as e:
#     print(f"Ошибка: {e}")

# try:
#     user = User(id=2, name="", birthday_date=date(2020, 1, 1))
#     print(user)
# except ValueError as e:
#     print(f"Ошибка: {e}")

# try:
#     user = User(id=3, name="Alice", birthday_date=date(1900, 1, 1))
#     print(user)
# except ValueError as e:
#     print(f"Ошибка: {e}")

#     @computed_field
#     def full_name(self) -> str:
#         return f"{self.name} {self.surname}"
    
#     @computed_field
#     def age(self) -> str:
#         today = date.today()
#         delta = relativedelta(today, self.birthday_date)
#         return f"{delta.years} лет, {delta.months} месяцев и {delta.days} дней."


# alex = User(
#     id=1,
#     name="Name",
#     surname="Surname",
#     birthday_date="1998-03-26"
# )

# print(alex.dict())