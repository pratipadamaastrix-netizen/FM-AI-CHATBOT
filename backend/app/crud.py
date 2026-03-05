# backend/app/crud.py
from sqlalchemy.orm import Session
from . import models, schemas, utils

def create_ticket(db: Session, ticket: schemas.TicketCreate):
    ticket_ref = utils.generate_ticket_ref()
    db_ticket = models.Ticket(
        reference=ticket_ref,
        user_name=ticket.user_name,
        location_estate=ticket.location_estate,
        location_unit=ticket.location_unit,
        problem_description=ticket.problem_description,
        category=ticket.category,
        priority=ticket.priority
    )
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket

def add_message(db: Session, message: schemas.MessageCreate):
    db_message = models.Message(**message.dict())
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message