from typing import Optional

from sqlalchemy import Float, ForeignKeyConstraint, Index, Integer, String, text
from sqlalchemy.orm import Mapped, mapped_column
from src.app.extensions import db




class PickerItem(db.Model):
    __tablename__ = 'picker_item'
    __table_args__ = (
        ForeignKeyConstraint(['list_id'], ['picker_list.id'], ondelete='CASCADE', onupdate='CASCADE', name='picker_item_ibfk_1'),
        Index('list_id', 'list_id')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    list_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    probability: Mapped[Optional[float]] = mapped_column(Float)

