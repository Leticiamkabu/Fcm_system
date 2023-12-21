from sqlalchemy import Boolean, Column, Integer, String, UUID, DateTime, func, JSON, ARRAY, text
from database.databaseConnection import Base
import datetime
from typing import List


class User(Base):
    __tablename__ = 'user'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text(
        "uuid_generate_v4()"), unique=True, index=True)
    name = Column(String, nullable=False)
    identification = Column(String, nullable=False)
    email = Column(String, nullable=True)
    phone = Column(String, nullable=False)
    identification_type = Column(String, nullable=False)
    date_of_birth = Column(String, nullable=False)
    address = Column(String, nullable=False)
    digital_address = Column(String, nullable=False)
    role = Column(String, nullable=False)
    nsId = Column(String, nullable=False)
    is_active = Column(Boolean, nullable=False, default=func.current_timestamp())
    created_on = Column(DateTime, nullable=False, default=func.current_timestamp())
    Updated_on = Column(DateTime, nullable=False, default=func.current_timestamp())
    created_by = Column(String, nullable=False)
    updated_by = Column(String, nullable=False)
