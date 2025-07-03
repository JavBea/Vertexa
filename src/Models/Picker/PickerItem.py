from typing import List, Optional

from sqlalchemy import DateTime, Enum, Float, ForeignKeyConstraint, Index, Integer, String, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
import datetime

from src.Models.Picker import PickerList


class Base(DeclarativeBase):
    pass


class PickerItem(Base):
    __tablename__ = 'picker_item'
    __table_args__ = (
        ForeignKeyConstraint(['list_id'], ['picker_list.id'], ondelete='CASCADE', onupdate='CASCADE', name='picker_item_ibfk_1'),
        Index('list_id', 'list_id')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    list_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    probability: Mapped[Optional[float]] = mapped_column(Float)

    list: Mapped['PickerList'] = relationship('PickerList', back_populates='picker_item')
