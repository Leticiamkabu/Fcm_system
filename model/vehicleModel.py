from sqlalchemy import Boolean, Column, Integer, String, UUID, DateTime, func, JSON, ARRAY, text
from database.databaseConnection import Base
import datetime
from typing import List


class Vehicle(Base):
    __tablename__ = 'vehicle'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text(
        "uuid_generate_v4()"), unique=True, index=True)
    vehicle_id = Column(String, nullable=False)
    allocated_liters = Column(String, nullable=False)
    balance = Column(String, nullable=True)
    vehicle_number_plate = Column(String, nullable=False)
    allocated_date = Column(String, nullable=False)
    created_on = Column(DateTime, nullable=False,
                        default=func.current_timestamp())
    created_by = Column(String, nullable=False)
    
