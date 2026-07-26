from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from database import Base
from datetime import datetime


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    client_name = Column(String, nullable=False)
    client_email = Column(String, nullable=False)
    subject = Column(String, nullable=False)
    description = Column(Text, default="")
    priority = Column(String, default="normal")
    status = Column(String, default="abierto")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class TicketMessage(Base):
    __tablename__ = "ticket_messages"

    id = Column(Integer, primary_key=True, index=True)
    ticket_id = Column(Integer, ForeignKey("tickets.id"), nullable=False)
    sender = Column(String, nullable=False)
    agent_name = Column(String, default="")
    message = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)