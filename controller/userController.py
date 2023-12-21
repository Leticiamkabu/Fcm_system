import os
from sqlalchemy.orm import Session
# from security.auth_bearer import jwtBearer
from database.databaseConnection import SessionLocal
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select, func, text
from model.userModel import User
from schema.userSchemas import *
import logging
from typing import Annotated
import uuid


# Console Logging
log_level = logging.INFO
if os.environ.get('DEBUG'):
    log_level = logging.DEBUG

logging.basicConfig(
    format='%(asctime)s %(levelname)s %(message)s', datefmt='%d/%m/%Y %I:%M:%S%p')


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

# create user
@router.post("/users/create_user")
async def create_user(user_data: UserCreation, db: db_dependency):
   
    forms_data = User(
            name=user_data.name,
            identification=user_data.identification,
            phone= user_data.phone,
            identification_type= user_data.identification_type,
            date_of_birth = user_data.date_of_birth,
            email = user_data.email,
            address= user_data.address,
            role = user_data.role,
            digital_address = user_data.digital_address,
            nsId = user_data.nsId,
            is_active = user_data.is_active,

        )


    async with db.begin():
        db.add(user_data)
        await db.commit()

    return {"message": "User  created successfully", "data": user_data}



# edit all user fields
@router.put("/users/update_all_user_fields/{id}")
async def update_user(id: uuid.UUID, db: db_dependency, user_input: UserCreation):
    user_data = await db.get(User, id)
    if user_data == None:
        raise HTTPException(
            status_code=200, detail="User is empty or null", data=user_data)
    results = user_input.__dict__
    for key, value in results.items():
        setattr(user_data, key, value)

    db.add(user_data)
    await db.commit()

    return user_data

#  Get all users
@router.get("/users/get_all_users")
async def get_all_users(db: db_dependency):
    result = await db.execute(select(User))
    user_data = result.scalars().all()

    if user_data is None:
        raise HTTPException(status_code=200, detail="User is empty or null", headers={
                            "message": "id listed in the user", "data": "[]"})

    return user_data





