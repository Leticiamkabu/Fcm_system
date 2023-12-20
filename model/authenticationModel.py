from sqlalchemy import Boolean, Column, Integer, String, UUID, DateTime, func, ARRAY, text
from database.databaseConnection import Base
import datetime


import random

def otp_generate():
    """ Function for generating a four-digit OTP """
    return str(random.randint(1000, 9999))

# Example usage:
otp = otp_generate()



class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text(
        "uuid_generate_v4()"), unique=True, index=True)
    first_name= Column(String, nullable=False)
    last_name= Column(String, nullable=False)
    email = Column(String, nullable=True)
    phone_number = Column(String, nullable=False)
    created_on = Column(DateTime, nullable=False, default=func.current_timestamp())




