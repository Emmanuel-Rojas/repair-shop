from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database import SessionLocal, engine, Base
from backend.models import Orden as OrdenModel
from backend.schemas import OrdenCreate, Orden

router = APIRouter()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/ordenes/", response_model=Orden)
def create_orden(orden: OrdenCreate, db: Session = Depends(get_db)):
    db_orden = OrdenModel(**orden.dict())
    db.add(db_orden)
    db.commit()
    db.refresh(db_orden)
    return db_orden

@router.get("/ordenes/{orden_id}", response_model=Orden)
def read_orden(orden_id: int, db: Session = Depends(get_db)):
    db_orden = db.query(OrdenModel).filter(OrdenModel.id == orden_id).first()
    if db_orden is None:
        raise HTTPException(status_code=404, detail="Orden no encontrada")
    return db_orden

@router.put("/ordenes/{orden_id}", response_model=Orden)
def update_orden(orden_id: int, orden: OrdenCreate, db: Session = Depends(get_db)):
    db_orden = db.query(OrdenModel).filter(OrdenModel.id == orden_id).first()
    if db_orden is None:
        raise HTTPException(status_code=404, detail="Orden no encontrada")
    for key, value in orden.dict().items():
        setattr(db_orden, key, value)
    db.commit()
    db.refresh(db_orden)
    return db_orden

@router.delete("/ordenes/{orden_id}")
def delete_orden(orden_id: int, db: Session = Depends(get_db)):
    db_orden = db.query(OrdenModel).filter(OrdenModel.id == orden_id).first()
    if db_orden is None:
        raise HTTPException(status_code=404, detail="Orden no encontrada")
    db.delete(db_orden)
    db.commit()
    return {"message": "Orden eliminada"}