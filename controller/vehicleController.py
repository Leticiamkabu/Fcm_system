import os
from sqlalchemy.orm import Session
# from security.auth_bearer import jwtBearer
from database.databaseConnection import SessionLocal
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select, func, text
from model.vehicleModel import Vehicle
from schema.vehicleSchema import *
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
       
        vehicle_number = vehicle_data.vehicle_number,
        vehicle_type = vehicle_data.vehicle_type,
        vehicle_model = vehicle_data.vehicle_model,
        driver_id = vehicle_data.driver_id,
        chasis_number = vehicle_data.chasis_number,
        fuel_capacity = vehicle_data.fuel_capacity,
        is_valid = vehicle_data.is_valid

        )


    async with db.begin():
        db.add(data)
        await db.commit()

    return {"message": "Vehicle  created successfully", "data": data}


# get vehicle by id
@router.get("/vehicle/{id}")
async def create_vehicle(id: str, db: db_dependency):
    vehicle_data = await db.get(Vehicle, id)
    
    return vehicle_data

# edit vehicle by id
@router.put("/vehicle/edit/{id}")
async def create_vehicle(id: str, db: db_dependency, vehicle_update_data: dict):
    vehicle_data = await db.get(Vehicle, id)
    
    if vehicle_data == None:
        raise HTTPException(status_code=200, detail="Form is empty or null", data = form_data)
    # results = vehicle_update_data.__dict__
    for key, value in vehicle_update_data.items():
        setattr(vehicle_data, key, value)
        
        
    db.add(vehicle_data)
    await db.commit()
    
    
    return vehicle_data
   

# delete  vehicle
@router.post("/vehicle/delete_vehicle/{id}")
async def create_vehicle(id: str, db: db_dependency):
    vehicle = await db.get(Vehicle, id)
  
    
    if not vehicle:
        raise HTTPException(
            status_code=404, 
            detail="Form not found",
            
        )
    
    await db.delete(vehicle)
    await db.commit()
    
    return "Vehicle data delete completed" 



