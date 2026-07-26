import logging
from fastapi import APIRouter, Depends, HTTPException, Query, Request
from sqlalchemy.orm import Session
from database import get_db
from models.price_range import PriceRange
from models.user import User
from modules.auth import require_admin_totp
from config import limiter

router = APIRouter(prefix="/api")
logger = logging.getLogger("xlink.api.prices")


@router.get("/prices", description="List active price ranges")
@limiter.limit("30/minute")
def list_prices(
    request: Request,
    db: Session = Depends(get_db),
):
    items = (
        db.query(PriceRange)
        .filter(PriceRange.active == True)
        .order_by(PriceRange.service.asc())
        .all()
    )
    return [
        {
            "id": p.id,
            "service": p.service,
            "min_price": p.min_price,
            "max_price": p.max_price,
            "unit": p.unit,
            "description": p.description,
            "active": p.active,
        }
        for p in items
    ]


@router.get("/admin/prices", description="List all price ranges (admin only)")
@limiter.limit("30/minute")
def admin_list_prices(
    request: Request,
    admin: User = Depends(require_admin_totp),
    db: Session = Depends(get_db),
):
    items = db.query(PriceRange).order_by(PriceRange.service.asc()).all()
    return [
        {
            "id": p.id,
            "service": p.service,
            "min_price": p.min_price,
            "max_price": p.max_price,
            "unit": p.unit,
            "description": p.description,
            "active": p.active,
        }
        for p in items
    ]


@router.post("/admin/prices", description="Create a price range (admin only)")
@limiter.limit("10/minute")
def admin_create_price(
    request: Request,
    body: dict,
    admin: User = Depends(require_admin_totp),
    db: Session = Depends(get_db),
):
    price = PriceRange(
        service=body.get("service", ""),
        min_price=body.get("min_price", 0),
        max_price=body.get("max_price", 0),
        unit=body.get("unit", "€"),
        description=body.get("description", ""),
        active=body.get("active", True),
    )
    db.add(price)
    db.commit()
    db.refresh(price)
    return {"id": price.id, "message": "Precio creado"}


@router.put("/admin/prices/{price_id}", description="Update a price range (admin only)")
@limiter.limit("10/minute")
def admin_update_price(
    request: Request,
    price_id: int,
    body: dict,
    admin: User = Depends(require_admin_totp),
    db: Session = Depends(get_db),
):
    price = db.query(PriceRange).filter(PriceRange.id == price_id).first()
    if not price:
        raise HTTPException(status_code=404, detail="Precio no encontrado")
    if "service" in body:
        price.service = body["service"]
    if "min_price" in body:
        price.min_price = body["min_price"]
    if "max_price" in body:
        price.max_price = body["max_price"]
    if "unit" in body:
        price.unit = body["unit"]
    if "description" in body:
        price.description = body["description"]
    if "active" in body:
        price.active = body["active"]
    db.commit()
    db.refresh(price)
    return {"id": price.id, "message": "Precio actualizado"}


@router.delete("/admin/prices/{price_id}", description="Delete a price range (admin only)")
@limiter.limit("10/minute")
def admin_delete_price(
    request: Request,
    price_id: int,
    admin: User = Depends(require_admin_totp),
    db: Session = Depends(get_db),
):
    price = db.query(PriceRange).filter(PriceRange.id == price_id).first()
    if not price:
        raise HTTPException(status_code=404, detail="Precio no encontrado")
    db.delete(price)
    db.commit()
    return {"ok": True}