import logging
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from database import get_db
from models.ticket import Ticket, TicketMessage
from models.user import User
from modules.auth import get_current_user, require_admin_totp
from config import limiter

router = APIRouter(prefix="/api")
logger = logging.getLogger("xlink.api.tickets")


@router.post("/tickets", description="Create a ticket (client)")
@limiter.limit("10/minute")
def create_ticket(
    request: Request,
    body: dict,
    db: Session = Depends(get_db),
):
    ticket = Ticket(
        user_id=body.get("user_id"),
        client_name=body.get("client_name", ""),
        client_email=body.get("client_email", ""),
        subject=body.get("subject", ""),
        description=body.get("description", ""),
        priority=body.get("priority", "normal"),
    )
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return {"id": ticket.id, "message": "Ticket creado"}


@router.get("/tickets", description="List my tickets (authenticated user)")
@limiter.limit("30/minute")
def list_my_tickets(
    request: Request,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    items = (
        db.query(Ticket)
        .filter(Ticket.user_id == user.id)
        .order_by(Ticket.updated_at.desc())
        .all()
    )
    return [
        {
            "id": t.id,
            "client_name": t.client_name,
            "client_email": t.client_email,
            "subject": t.subject,
            "priority": t.priority,
            "status": t.status,
            "created_at": str(t.created_at)[:19],
            "updated_at": str(t.updated_at)[:19],
        }
        for t in items
    ]


@router.get("/tickets/{ticket_id}", description="Ticket detail with messages")
@limiter.limit("30/minute")
def get_ticket(
    request: Request,
    ticket_id: int,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket no encontrado")
    if ticket.user_id != user.id and user.role != "admin":
        raise HTTPException(status_code=403, detail="No tienes acceso a este ticket")
    messages = (
        db.query(TicketMessage)
        .filter(TicketMessage.ticket_id == ticket_id)
        .order_by(TicketMessage.created_at.asc())
        .all()
    )
    return {
        "id": ticket.id,
        "client_name": ticket.client_name,
        "client_email": ticket.client_email,
        "subject": ticket.subject,
        "description": ticket.description,
        "priority": ticket.priority,
        "status": ticket.status,
        "created_at": str(ticket.created_at)[:19],
        "updated_at": str(ticket.updated_at)[:19],
        "messages": [
            {
                "id": m.id,
                "sender": m.sender,
                "agent_name": m.agent_name,
                "message": m.message,
                "created_at": str(m.created_at)[:19],
            }
            for m in messages
        ],
    }


@router.post("/tickets/{ticket_id}/messages", description="Add a message to a ticket (client)")
@limiter.limit("10/minute")
def add_ticket_message(
    request: Request,
    ticket_id: int,
    body: dict,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket no encontrado")
    if ticket.user_id != user.id:
        raise HTTPException(status_code=403, detail="No tienes acceso a este ticket")
    msg = TicketMessage(
        ticket_id=ticket_id,
        sender="client",
        agent_name="",
        message=body.get("message", ""),
    )
    db.add(msg)
    ticket.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(msg)
    return {"id": msg.id, "message": "Mensaje añadido"}


@router.get("/admin/tickets", description="List all tickets (admin only)")
@limiter.limit("30/minute")
def admin_list_tickets(
    request: Request,
    admin: User = Depends(require_admin_totp),
    db: Session = Depends(get_db),
):
    items = db.query(Ticket).order_by(Ticket.updated_at.desc()).all()
    return [
        {
            "id": t.id,
            "user_id": t.user_id,
            "client_name": t.client_name,
            "client_email": t.client_email,
            "subject": t.subject,
            "priority": t.priority,
            "status": t.status,
            "created_at": str(t.created_at)[:19],
            "updated_at": str(t.updated_at)[:19],
        }
        for t in items
    ]


@router.put("/admin/tickets/{ticket_id}", description="Update ticket status/priority (admin only)")
@limiter.limit("10/minute")
def admin_update_ticket(
    request: Request,
    ticket_id: int,
    body: dict,
    admin: User = Depends(require_admin_totp),
    db: Session = Depends(get_db),
):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket no encontrado")
    if "status" in body:
        ticket.status = body["status"]
    if "priority" in body:
        ticket.priority = body["priority"]
    ticket.updated_at = datetime.utcnow()
    db.commit()
    return {"id": ticket.id, "message": "Ticket actualizado"}


@router.post("/admin/tickets/{ticket_id}/messages", description="Reply as admin")
@limiter.limit("10/minute")
def admin_reply_ticket(
    request: Request,
    ticket_id: int,
    body: dict,
    admin: User = Depends(require_admin_totp),
    db: Session = Depends(get_db),
):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket no encontrado")
    msg = TicketMessage(
        ticket_id=ticket_id,
        sender="agent",
        agent_name=admin.name,
        message=body.get("message", ""),
    )
    db.add(msg)
    ticket.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(msg)
    return {"id": msg.id, "message": "Respuesta enviada"}