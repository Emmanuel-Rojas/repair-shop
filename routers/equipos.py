from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import Equipo
from schemas import EquipoCreate, Equipo

router = APIRouter()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/equipos/", response_model=Equipo)
def create_equipo(equipo: EquipoCreate, db: Session = Depends(get_db)):
    db_equipo = Equipo(**equipo.dict())
    db.add(db_equipo)
    db.commit()
    db.refresh(db_equipo)
    return db_equipo

@router.get("/equipos/{equipo_id}", response_model=Equipo)
def read_equipo(equipo_id: int, db: Session = Depends(get_db)):
    db_equipo = db.query(Equipo).filter(Equipo.id == equipo_id).first()
    if db_equipo is None:
        raise HTTPException(status_code=404, detail="Equipo no encontrado")
    return db_equipo

@router.put("/equipos/{equipo_id}", response_model=Equipo)
def update_equipo(equipo_id: int, equipo: EquipoCreate, db: Session = Depends(get_db)):
    db_equipo = db.query(Equipo).filter(Equipo.id == equipo_id).first()
    if db_equipo is None:
        raise HTTPException(status_code=404, detail="Equipo no encontrado")
    for key, value in equipo.dict().items():
        setattr(db_equipo, key, value)
    db.commit()
    db.refresh(db_equipo)
    return db_equipo

@router.delete("/equipos/{equipo_id}")
def delete_equipo(equipo_id: int, db: Session = Depends(get_db)):
    db_equipo = db.query(Equipo).filter(Equipo.id == equipo_id).first()
    if db_equipo is None:
        raise HTTPException(status_code=404, detail="Equipo no encontrado")
    db.delete(db_equipo)
    db.commit()
    return {"message": "Equipo eliminado"}
