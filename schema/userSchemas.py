from pydantic import BaseModel


class UserCreation(BaseModel):
    name: str
    identification: str
    phone: str
    identification_type:str
    date_of_birth: str
    email: str
    address: str
    role: str
    digital_address: str
    nsId: str
    is_active: str
    # updated_by: str
    