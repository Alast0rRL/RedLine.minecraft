# app/models.py
from sqlalchemy import Column, Integer, String, DateTime
from .database import Base
from datetime import datetime

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    first_login = Column(DateTime, default=datetime.utcnow)
    play_time_minutes = Column(Integer, default=0)