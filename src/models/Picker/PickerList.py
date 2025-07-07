from typing import Optional

from sqlalchemy import DateTime, Enum, Integer, String, text
from sqlalchemy.orm import Mapped, mapped_column
import datetime
from src.app.extensions import db

class PickerList(db.Model):
    __tablename__ = 'picker_list'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    availability: Mapped[str] = mapped_column(Enum('available', 'unavailable'), server_default=text("'available'"))
    created_time: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
