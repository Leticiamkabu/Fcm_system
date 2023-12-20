from fastapi import APIRouter, Depends, HTTPException, status
from model.authenticationModel import *
from schema.authenticationSchema import *
from typing import Annotated
from sqlalchemy.orm import Session
from database.databaseConnection import SessionLocal
import uuid
import logging
import os
from sqlalchemy import select, update
from fastapi.encoders import jsonable_encoder
import base64
import requests



#Console Logging
log_level = logging.INFO
if os.environ.get('DEBUG'):
    log_level = logging.DEBUG

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', datefmt='%d/%m/%Y %I:%M:%S%p')

# logging.basicConfig(filename="auth.log", level=logging.DEBUG,
#     format='%(asctime)s %(levelname)s %(message)s', datefmt='%d/%m/%Y %I:%M:%S%p')
logger = logging.getLogger(__name__)



# create a connection to the database
async def get_db():
    db = SessionLocal()
    try:
        yield db

    finally:
        await db.close()

db_dependency = Annotated[Session, Depends(get_db)]




router = APIRouter()




 

# new method
@router.post("/auth/login")
async def login(login: Login, db: db_dependency):
    user = await db.execute(select(User).where(User.phone_number == login.phone))
    user_data = user.scalar()
   
#   sms endpoint
    bearer_token = os.getenv('BEARER_TOKEN')
    sms_url = os.getenv('HUBTEL_SMS_ENDPOINT')
        
            
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {bearer_token}",
        "accept": "text/plain"
            }
            
    payload = {
            "From": "MySay", 
            "To": login.phone
            
        }
        # print(payload)
    try:
        response = requests.post(sms_url, json=payload, headers=headers)

        if response.status_code == 200:
            return {"message": "SMS sent successfully"}
        else:
            raise HTTPException(status_code=response.status_code, detail="Failed to send SMS")

    except Exception as e:
            
        raise HTTPException(status_code=501, detail=f"Internal server error: {str(e)}")
        
    



@router.post("/auth/verify_otp")
async def verify_otp(otp:Otp_verification , db: db_dependency):
   
#    otp verification endpoint
    bearer_token = os.getenv('BEARER_TOKEN')
    sms_url = os.getenv('OTP_VERIFICATION_LINK_URL')
        
            
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {bearer_token}",
        "accept": "text/plain"
        }
            
    payload = {
        "phone": otp.phone,  
        "code": otp.code
            
    }
        
    try:
        response = requests.post(sms_url, json=payload, headers=headers)

        if response.status_code == 200:
            user = await db.execute(select(User).where(User.phone_number == otp.phone))
            user_data = user.scalar()
           
            return {"message": "OTP verification successful", "user": user_data }
        else:
            raise HTTPException(status_code=response.status_code, detail="Failed to verify OTP")

    except Exception as e:
            
        raise HTTPException(status_code=501, detail=f"Internal server error: {str(e)}")
        
    


