# # models

# from pydantic import BaseModel


# class ExampleUser(BaseModel):
#     id: int
#     name: str
#     age: int = 18


# # data validator
# # validate_user = ExampleUser(
# #     id='first',
# #     name='Alice',
# #     age=25
# # )

# # data converter
# # convert_user = ExampleUser(
# #     id="1",
# #     name='Alice',
# #     age = '25'
# # )

# # complex models
# class Address(BaseModel):
#     street: str
#     city: str


# class UserWithAddress(BaseModel):
#     id: int
#     name: str
#     address: Address


# # address = Address(
# #     street='123 Main St',
# #     city='New New'
# # )

# # user = UserWithAddress(
# #     id=1,
# #     name='Alice',
# #     address=address
# # )

# # validate user data types
# from pydantic import field_validator


# class UserWithValidation(BaseModel):
#     id: int
#     name: str
#     age: int

#     @field_validator('age')
#     def check_age(cls, v):
#         if v < 18:
#             raise ValueError('Age must be at least 18')
#         return v


# # user = UserWithValidation(
# #     id=1,
# #     name='Alice',
# #     age=25
# # )

# # The basic of Pydantic

# # Numberic types

# from pydantic import BaseModel #, Decimal


# class Product(BaseModel):
#     id: int
#     price: float
#     # tax: Decimal


# # String types

# class StringUser(BaseModel):
#     username: str
#     first_name: str
#     last_name: str


# # Boolean types

# class FeatureFlag(BaseModel):
#     is_enabled: bool


# # Lists and tuples

# class Order(BaseModel):
#     items: list[str]
#     quantities: tuple[int, int, int]

# # Dicts

# class Config(BaseModel):
#     settings: dict[str, str]

# # Date and time

# from datetime import datetime, timedelta

# class Event(BaseModel):
#     start_datetime: datetime
#     end_datetime: datetime
#     duration: timedelta

# # UUID

# from uuid import UUID

# class Item(BaseModel):
#     id: UUID
#     name: str

# # Emails and URLs
# from pydantic import EmailStr, AnyUrl

# class Contact(BaseModel):
#     email: EmailStr
#     website: AnyUrl


from datetime import datetime
from uuid import UUID, uuid4

# Data models
from pydantic import BaseModel, EmailStr, Field, field_validator

# class User(BaseModel):
#     id: UUID
#     username: str
#     email: EmailStr
#     is_active: bool = True
#     created_at: datetime = datetime.now()


# try:
#     user = User(
#         id=uuid4(), # 'not-a-uuid'
#         username='alice',
#         email='alice@example.com'
#     )
#     print(user)
#     user_json = user.model_dump_json()
#     print(user_json)
# except ValueError as e:
#     print(e)

# Complex data models


class Address(BaseModel):
    street: str
    city: str
    country: str


class UserWithAddress(BaseModel):
    id: UUID
    username: str
    email: str
    address: Address


user = UserWithAddress(
    id=uuid4(),
    username="alice",
    email="alice@example.com",
    address=Address(
        street="123 Main St",
        city="New York",
        country="USA",
    ),
)


class Product(BaseModel):
    id: UUID
    name: str
    price: float
    tags: list[str] = []
    metadata: dict[str, str] = {}


class User(BaseModel):
    id: UUID
    username: str
    email: str = Field(alias="user_email")
    is_active: bool = True
    created_at: datetime = datetime.now()

    @field_validator("age")
    def check_age(cls, v):
        if v < 18:
            raise ValueError("Age must be at least 18")
        return v
