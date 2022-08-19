import databases
import os
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from sqlalchemy import insert, select, update, delete
from sqlalchemy import Table, Column, Integer, String, create_engine
from sqlalchemy import create_engine
from sqlalchemy import MetaData

DATABASE_URL = ('sqlite:///clientes.db')


metadata = MetaData()

clientes = Table(
    'clientes', metadata,
    Column('id_cliente', Integer, primary_key=True),
    Column('nombre',String, nullable=False),
    Column('email',String, nullable=False)
)

database = databases.Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)
metadata.create_all(engine)

class Respuesta(BaseModel):
    message: str


class Cliente(BaseModel):
    id_cliente: int
    nombre: str
    email: str

class ClienteIN(BaseModel):
    nombre: str
    email: str

app = FastAPI()

@app.get("/", response_model=Respuesta)
async def index():
    return {"message": "API-REST"}

@app.get("/clientes", response_model=List[Cliente])
async def get_clientes():
    query = select(clientes)
    return await database.fetch_all(query)

@app.get("/clientes/{id_clientes}", response_model=Cliente)
async def get_clientes(id_cliente: int):
    query = select(clientes).where(clientes.c.id_cliente == id_cliente)
    return await database.fetch_one(query)

@app.post("/clientes", response_model=Respuesta)
async def create_clientes(cliente: ClienteIN):
    query = insert(clientes).values(nombre=cliente.nombre, email=cliente.email)
    await database.execute(query)
    return{"message":"Cliente creado"}

@app.put("/clientes/{id_clientes}", response_model=Respuesta)
async def update_clientes(id_cliente: int, cliente: ClienteIN):
    query = update(clientes).where(clientes.c.id_cliente == id_cliente).values(nombre=cliente.nombre, email=cliente.email)
    await database.execute(query)
    return{"message":"Cliente actualizado"}

@app.delete("/clientes/{id_clientes}", response_model=Respuesta)
async def delete_clientes(id_cliente: int):
    query = delete(clientes).where(clientes.c.id_cliente == id_cliente)
    await database.execute(query)
    return{"message":"Cliente Eliminado"}
