from pydantic import BaseModel


class ParentModel(BaseModel):
    name: str
    age: int

    
class ChildModel(ParentModel):
    school: str

    
parent = ParentModel(
    name="Alex",
    age=40
    )
child = ChildModel(
    name="Bob",
    age=12,
    school="Greenwood High"
    )