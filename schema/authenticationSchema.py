from pydantic import BaseModel

class UserCreation(BaseModel):
    email:str
    first_name:str
    last_name:str
    phone_number:str


class Login(BaseModel):
    phone:str
    

class Otp_verification(BaseModel):
    phone:str
    code:str

# test
class UserLoginSchema(BaseModel):
    username: str
    password: str
    

# class AuthData(BaseModel):
#     user_id: str