from sqlalchemy import Boolean, Column, Integer, String, UUID, DateTime, func, JSON, ARRAY, text
from database.databaseConnection import Base
import datetime
from typing import List


class User(Base):
    __tablename__ = 'user'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text(
        "uuid_generate_v4()"), unique=True, index=True)
    fname = Column(String, nullable=False)
    lname = Column(String, nullable=False)
    email = Column(String, nullable=True)
    phone_number = Column(String, nullable=False)
    role = Column(String, nullable=False)
    created_on = Column(DateTime, nullable=False,
                        default=func.current_timestamp())
    updated_on = Column(DateTime, nullable=False, default=func.current_timestamp())
    created_by = Column(String, nullable=False)
    updated_by = Column(String, nullable=False)
