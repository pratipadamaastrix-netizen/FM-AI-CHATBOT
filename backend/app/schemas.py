# backend/app/schemas.py
from pydantic import BaseModel

# -------------------------------
# Ticket schemas
# -------------------------------
class TicketCreate(BaseModel):
    user_name: str
    location_estate: str
    location_unit: str
    problem_description: str
    category: str
    priority: str

class Ticket(TicketCreate):
    id: int
    reference: str
    status: str
    created_at: str
    updated_at: str | None = None

    class Config:
        from_attributes = True  # ✅ replaces orm_mode in Pydantic v2

# -------------------------------
# Message schemas
# -------------------------------
class MessageCreate(BaseModel):
    ticket_id: int
    sender_role: str
    content: str
    visible_to_customer: bool = True

class Message(MessageCreate):
    id: int
    timestamp: str

    class Config:
        from_attributes = True  # ✅ replaces orm_mode