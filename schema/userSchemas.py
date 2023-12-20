from pydantic import BaseModel


class UserCreation(BaseModel):
    email: str
    fname: str
    lname: str
    email:str
    role: str
    phone_number: str
    created_by: str
    # updated_by: str
    