from sqlalchemy import Column, BigInteger, String, Boolean

from utils.db import Base
from utils.db.db_tool import DBTool
from utils.db.mixins import TimestampMixin


class User(Base, TimestampMixin, DBTool):
    __tablename__ = "user"
    
    id = Column(BigInteger, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String)
    
    role = Column(String, default="user")
    banned = Column(Boolean, default=False)
