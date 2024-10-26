from src.db.models.base import Base
from sqlalchemy import VARCHAR, CHAR
from sqlalchemy.orm import mapped_column
from sqlalchemy import Column
from sqlalchemy import UUID

from uuid import uuid4

class User(Base):
    __tablename__ = "user"
    
    id = Column(UUID(), default=uuid4, primary_key=True)
    name = mapped_column(VARCHAR(255), nullable=False)
    link = mapped_column(CHAR(500))
