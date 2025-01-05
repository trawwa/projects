# models

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    age: int = 18


# data validator
validate_user = User(
    id='first', 
    name='Alice', 
    age=25
)

# data converter
convert_user = User(
    id="1",
    name='Alice',
    age = '25'
)

# complex models
class Address(BaseModel):
    street: str
    city: str


class UserWithAddress(BaseModel):
    id: int
    name: str
    address: Address


address = Address(
    street='123 Main St',
    city='New New'
)

user = UserWithAddress(
    id=1,
    name='Alice',
    address=address
)

# validate user data types
from pydantic import field_validator


class UserWithValidation(BaseModel):
    id: int
    name: str
    age: int

    @field_validator('age')
    def check_age(cls, v):
        if v < 18:
            raise ValueError('Age must be at least 18')
        return v
    

user = UserWithValidation(
    id=1,
    name='Alice',
    age=25
)