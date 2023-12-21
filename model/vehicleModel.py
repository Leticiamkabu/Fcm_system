from sqlalchemy import Boolean, Column, Integer, String, UUID, DateTime, func, JSON, ARRAY, text
from database.databaseConnection import Base
import datetime
from typing import List


class Vehicle(Base):
    __tablename__ = 'vehicle'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text(
        "uuid_generate_v4()"), unique=True, index=True)
    vehicle_number = Column(String, nullable=False)
    vehicle_type = Column(String, nullable=False)
    vehicle_model = Column(String, nullable=True)
    driver_id = Column(String, nullable=False)
    chasis_number = Column(String, nullable=False)
    fuel_capacity = Column(String, nullable=False)
    is_valid = Column(Boolean, nullable=False)
    created_on = Column(DateTime, nullable=False,
                        default=func.current_timestamp())
    updated_on = Column(DateTime, nullable=False,
                        default=func.current_timestamp())
    created_by = Column(String, nullable=False)
    updated_by = Column(String, nullable=False)
    


class Entitlement(Base):
    __tablename__ = 'entitlements'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text(
        "uuid_generate_v4()"), unique=True, index=True)
    vehicle_id = Column(String, nullable=False)
    allocation_days = Column(Integer, nullable=False)
    allocation_cap = Column(Integer, nullable=True)
    allocation_bal = Column(Integer, nullable=False)
    last_fueling_date = Column(DateTime, nullable=False,
                        default=func.current_timestamp())
    created_on = Column(DateTime, nullable=False,
                        default=func.current_timestamp())
    updated_on = Column(DateTime, nullable=False,
                        default=func.current_timestamp())
    created_by = Column(String, nullable=False)
    updated_by = Column(String, nullable=False)
    
    
    
class Fuelings(Base):
    __tablename__ = 'fuelings'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text(
        "uuid_generate_v4()"), unique=True, index=True)
    vehicle_id = Column(String, nullable=False)
    amount_allocated = Column(String, nullable=True)
    created_on = Column(DateTime, nullable=False,
                        default=func.current_timestamp())
    