from fastapi import APIRouter, Depends, Form, UploadFile, File
from sqlalchemy.orm import Session
from typing import Optional
from .. import crud, schemas, database, ai_integration, utils

router = APIRouter()

# words that indicate a real maintenance issue
ISSUE_KEYWORDS = [
    "not working", "broken", "fault", "leak",
    "smell", "sparks", "shock", "malfunction",
    "water", "ac", "lift", "electric", "damage"
]


@router.post("/chat")
async def chat(
    user_name: str = Form(...),
    location_estate: str = Form(...),
    location_unit: str = Form(...),
    problem_description: str = Form(...),
    file: Optional[UploadFile] = File(None),
    db: Session = Depends(database.get_db)
):
    try:

        description = problem_description

        # -----------------------------
        # FILE HANDLING
        # -----------------------------
        if file:
            file_content = await file.read()
            print("File received:", file.filename)

            # optional: save file
            # with open(f"uploads/{file.filename}", "wb") as f:
            #     f.write(file_content)

        # -----------------------------
        # AI CHAT RESPONSE
        # -----------------------------
        try:
            ai_reply = ai_integration.chat_with_ai(description)
        except Exception as e:
            print("AI ERROR:", e)
            ai_reply = "I'm having trouble understanding the issue right now."

        # -----------------------------
        # DETECT IF ISSUE REQUIRES TICKET
        # -----------------------------
        issue_detected = any(word in description.lower() for word in ISSUE_KEYWORDS)

        ticket_reference = None

        if issue_detected:

            # AI classification
            try:
                category = ai_integration.classify_issue(description)
            except:
                category = "General"

            # priority mapping
            priority = utils.map_priority(description)

            # create ticket
            ticket_data = schemas.TicketCreate(
                user_name=user_name,
                location_estate=location_estate,
                location_unit=location_unit,
                problem_description=description,
                category=category,
                priority=priority
            )

            ticket = crud.create_ticket(db, ticket_data)

            ticket_reference = ticket.reference

            # append ticket confirmation to AI reply
            ai_reply += f"""

Ticket Created Successfully

Reference: {ticket.reference}
Category: {ticket.category}
Priority: {ticket.priority}

Our maintenance team has been notified.
"""

        # -----------------------------
        # SAVE CHAT MESSAGE
        # -----------------------------
        if ticket_reference:
            crud.add_message(
                db,
                schemas.MessageCreate(
                    ticket_id=ticket.id,
                    sender_role="user",
                    content=description
                )
            )

            crud.add_message(
                db,
                schemas.MessageCreate(
                    ticket_id=ticket.id,
                    sender_role="bot",
                    content=ai_reply
                )
            )

        return {
            "ticket_reference": ticket_reference,
            "bot_reply": ai_reply
        }

    except Exception as e:
        print("SERVER ERROR:", str(e))
        return {"bot_reply": "Internal Server Error"}