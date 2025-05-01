from pydantic import BaseModel

class ClienteBase(BaseModel):
    nombre: str
    direccion: str
    telefono: str
    email: str

class ClienteCreate(ClienteBase):
    pass

class Cliente(ClienteBase):
    id: int
    equipos: list = []

    class Config:
        from_attributes = True

class EquipoBase(BaseModel):
    marca: str
    modelo: str
    numero_serie: str

class EquipoCreate(EquipoBase):
    propietario_id: int

class Equipo(EquipoBase):
    id: int
    propietario_id: int
    ordenes: list = []

    class Config:
        from_attributes = True

class OrdenBase(BaseModel):
    descripcion: str
    estado: str
    costo: int

class OrdenCreate(OrdenBase):
    equipo_id: int

class Orden(OrdenBase):
    id: int
    equipo_id: int

    class Config:
        from_attributes = True
