import logging
from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from database import get_db
from models.project_gallery import ProjectGallery
from models.user import User
from modules.auth import require_admin_totp
from config import limiter

router = APIRouter(prefix="/api")
logger = logging.getLogger("xlink.api.gallery")


@router.get("/gallery", description="List public gallery projects")
@limiter.limit("30/minute")
def list_gallery(
    request: Request,
    db: Session = Depends(get_db),
):
    items = (
        db.query(ProjectGallery)
        .order_by(ProjectGallery.featured.desc(), ProjectGallery.created_at.desc())
        .all()
    )
    return [
        {
            "id": g.id,
            "title": g.title,
            "description": g.description,
            "client_name": g.client_name,
            "image_data": g.image_data,
            "category": g.category,
            "featured": g.featured,
            "created_at": str(g.created_at)[:19],
        }
        for g in items
    ]


@router.get("/gallery/{gallery_id}", description="Get gallery project detail")
@limiter.limit("30/minute")
def get_gallery_item(
    request: Request,
    gallery_id: int,
    db: Session = Depends(get_db),
):
    item = db.query(ProjectGallery).filter(ProjectGallery.id == gallery_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    return {
        "id": item.id,
        "title": item.title,
        "description": item.description,
        "client_name": item.client_name,
        "image_data": item.image_data,
        "category": item.category,
        "featured": item.featured,
        "created_at": str(item.created_at)[:19],
    }


@router.get("/admin/gallery", description="List all gallery projects (admin only)")
@limiter.limit("30/minute")
def admin_list_gallery(
    request: Request,
    admin: User = Depends(require_admin_totp),
    db: Session = Depends(get_db),
):
    items = db.query(ProjectGallery).order_by(ProjectGallery.created_at.desc()).all()
    return [
        {
            "id": g.id,
            "title": g.title,
            "description": g.description,
            "client_name": g.client_name,
            "image_data": g.image_data,
            "category": g.category,
            "featured": g.featured,
            "created_at": str(g.created_at)[:19],
        }
        for g in items
    ]


@router.post("/admin/gallery", description="Create a gallery project (admin only)")
@limiter.limit("10/minute")
def admin_create_gallery(
    request: Request,
    body: dict,
    admin: User = Depends(require_admin_totp),
    db: Session = Depends(get_db),
):
    project = ProjectGallery(
        title=body.get("title", ""),
        description=body.get("description", ""),
        client_name=body.get("client_name", ""),
        image_data=body.get("image_data", ""),
        category=body.get("category", "general"),
        featured=body.get("featured", False),
    )
    db.add(project)
    db.commit()
    db.refresh(project)
    return {"id": project.id, "message": "Proyecto creado"}


@router.delete("/admin/gallery/{gallery_id}", description="Delete a gallery project (admin only)")
@limiter.limit("10/minute")
def admin_delete_gallery(
    request: Request,
    gallery_id: int,
    admin: User = Depends(require_admin_totp),
    db: Session = Depends(get_db),
):
    project = db.query(ProjectGallery).filter(ProjectGallery.id == gallery_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    db.delete(project)
    db.commit()
    return {"ok": True}