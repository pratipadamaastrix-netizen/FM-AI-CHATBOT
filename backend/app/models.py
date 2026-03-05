# backend/app/models.py
from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from sqlalchemy.sql import func
from .database import Base  # relative import

class Ticket(Base):
    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True, index=True)
    reference = Column(String, unique=True, index=True)
    user_name = Column(String)
    location_estate = Column(String)
    location_unit = Column(String)
    problem_description = Column(Text)
    category = Column(String)
    priority = Column(String)
    status = Column(String, default="OPEN")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    ticket_id = Column(Integer)
    sender_role = Column(String)  # user / bot
    content = Column(Text)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    visible_to_customer = Column(Boolean, default=True)