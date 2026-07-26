from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime
from database import Base
from datetime import datetime


class ProjectGallery(Base):
    __tablename__ = "project_gallery"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, default="")
    client_name = Column(String, default="")
    image_data = Column(Text, nullable=False)
    category = Column(String, default="general")
    featured = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)