from typing import Optional
from sqlalchemy import Column, Float, ForeignKeyConstraint, Index, Integer, String, text
from src.app.extensions import db

class PickerItem(db.Model):
    __tablename__ = 'picker_item'
    __table_args__ = (
        ForeignKeyConstraint(
            ['list_id'],
            ['picker_list.id'],
            ondelete='CASCADE',
            onupdate='CASCADE',
            name='picker_item_ibfk_1'
        ),
        Index('list_id', 'list_id')
    )

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    list_id = Column(Integer, primary_key=True)
    probability = Column(Float, nullable=True)