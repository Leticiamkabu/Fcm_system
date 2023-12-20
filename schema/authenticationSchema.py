from pydantic import BaseModel

class Login(BaseModel):
    phone:str
    

class Otp_verification(BaseModel):
    phone:str
    code:str
