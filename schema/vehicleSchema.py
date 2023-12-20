from pydantic import BaseModel


class VehicleCreation(BaseModel):
    vehicle_id: str
    allocated_liters: str
    vehicle_number_plate: str
    allocated_date: str
    balance: str
    created_by: str
    # updated_by: str
