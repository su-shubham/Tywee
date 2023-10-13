from pydantic import BaseModel, EmailStr, constr


class User(BaseModel):
    name: constr(max_length=40)
    email: EmailStr
    password: str


class Display_user(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True
