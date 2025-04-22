from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    direccion = Column(String)
    telefono = Column(String)
    email = Column(String)

    equipos = relationship("Equipo", back_populates="propietario")

class Equipo(Base):
    __tablename__ = 'equipos'
    id = Column(Integer, primary_key=True, index=True)
    marca = Column(String)
    modelo = Column(String)
    numero_serie = Column(String)
    propietario_id = Column(Integer, ForeignKey('clientes.id'))

    propietario = relationship("Cliente", back_populates="equipos")
    ordenes = relationship("Orden", back_populates="equipo")

class Orden(Base):
    __tablename__ = 'ordenes'
    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String)
    estado = Column(String)
    costo = Column(Integer)
    equipo_id = Column(Integer, ForeignKey('equipos.id'))

    equipo = relationship("Equipo", back_populates="ordenes")
