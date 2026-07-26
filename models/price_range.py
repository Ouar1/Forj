from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base


class PriceRange(Base):
    __tablename__ = "price_ranges"

    id = Column(Integer, primary_key=True, index=True)
    service = Column(String, nullable=False)
    min_price = Column(Float, default=0)
    max_price = Column(Float, default=0)
    unit = Column(String, default="€")
    description = Column(String, default="")
    active = Column(Boolean, default=True)