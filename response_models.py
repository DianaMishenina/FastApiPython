from pydantic import BaseModel

class UserCreate(BaseModel):
    name:str
    role:str

class UserUpdate(BaseModel):
    name:str = None
    role_id:int = 1

class RoleCreate(BaseModel):
    name:str

class UserRead(BaseModel):
    id:int
    name:str
    role_id:int

class RoleRead(BaseModel):
    id:int
    name:int

