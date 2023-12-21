from pydantic import BaseModel


class VehicleCreation(BaseModel):
    vehicle_number: str
    vehicle_type: str
    vehicle_number_plate: str
    vehicle_model: str
    driver_id: str
    chasis_number: str
    fuel_capacity:str
    is_valid:str
    
    
class AllocationCreation(BaseModel):
    vehicle_id: str
    allocation_days: str
    allocation_cap: str
    allocation_bal: str
    lastFueling_date: str
