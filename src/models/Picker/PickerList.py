from datetime import datetime
from typing import Optional

from sqlalchemy import Column, DateTime, Enum, Integer, String, text
from src.app.extensions import db

class PickerList(db.Model):
    __tablename__ = 'picker_list'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    availability = Column(Enum('available', 'unavailable'), server_default=text("'available'"))
    created_time = Column(DateTime, nullable=True)