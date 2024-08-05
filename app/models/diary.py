from sqlalchemy import BigInteger, Column, ForeignKey, Integer
from utils.db import Base
from utils.db.db_tool import DBTool
from utils.db.mixins import TimestampMixin


class DiaryRecord(Base, TimestampMixin, DBTool):
    __tablename__ = "diary_record"

    id = Column(BigInteger, autoincrement=True, primary_key=True)
    user_id = Column(BigInteger, ForeignKey("user.id"), primary_key=True)
    calories = Column(Integer)
    protein = Column(Integer)
    fats = Column(Integer)
    carbs = Column(Integer)
