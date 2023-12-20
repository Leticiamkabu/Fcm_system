import os
from sqlalchemy.orm import Session
# from security.auth_bearer import jwtBearer
from database.databaseConnection import SessionLocal
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select, func, text
from models.vehicleModel import Vehicle
from schemas import vehicleSchema
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


# create vehicle
@router.post("/vehicle/create_vehicle")
async def create_vehicle(vehicle_data: VehicleCreation, db: db_dependency):
   
    data = Vehicle(
        vehicle_id=vehicle_data.vehicle_id,
        allocated_liters=user_vehicle_data.allocated_liters,
        vehicle_number_plate=vehicle_data.vehicle_number_plate,
        allocated_date=vehicle_data.allocated_date,
        balance=vehicle_data.balance,
        created_by=vehicle_data.created_by,

        )


    async with db.begin():
        db.add(data)
        await db.commit()

    return {"message": "Vehicle  created successfully", "data": data}
