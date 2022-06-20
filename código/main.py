from fastapi import FastAPI
import sqlite3
from typing import List
from pydantic import BaseModel

class Respuesta(BaseModel):
    message: str


class Cliente(BaseModel):
    id_cliente: int
    nombre: str 
    email: str

app = FastAPI()

#3.123
@app.get("/", response_model=Respuesta)
def index():
    return {"message": "Hello World"}

@app.get("/clientes/", response_model=List[Cliente])
async def clientes():
    with sqlite3.connect('sql/clientes.sqlite')as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM clientes")
        response = cursor.fetchall()
        return response
        


@app.get("/clientes/{id_cliente}", response_model=Cliente)
async def clientes():
    with sqlite3.connect('sql/clientes.sqlite')as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM clientes")
        response = cursor.fetchone()
        return response

"""
@app.get("/clientes/" , response_model=List[Cliente])
async def get_clientes(offset:int=0,limit:int=10):
    cursor.execute("SELECT * FROM clientes OFFSET ? LIMIT ?", (offset,limit))

@app.post("/clientes/")
def post_clientes(nombre: str, email:str):
    return f"Clientes {nombre} {email} almacenado"

@app.put("/clientes/")
def put_clientes(nombre: str, email:str):
    return f"Clientes {nombre} {email} actualizado"

@app.delete("/clientes/{id_clientes}")
def delete_clientes(id_clientes: int):
    return f"Clientes {id_clientes} eliminado"

"""


@app.post("/clientes/", response_model=Respuesta)
async def post_cliente(cliente=Cliente):
    with sqlite3.connect('sql/clientes.sqlite') as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("INSERT INTO clientes (nombre,email VALUES (4,'addair','addair@email.com')",
        (Cliente.id_clientes,Cliente.nombre,Cliente.email))
        connection.commit()
        connection.close()
        return {"message": "ALMACENADO"}

@app.put("/clientes/", response_model=Respuesta)
async def put_cliente(cliente=Cliente):
    with sqlite3.connect('sql/clientes.sqlite') as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("UPDATE clientes SET nombre = addair, email = addair99@email.com WHERE id_clientes = 4')",
        (cliente.id_clientes,cliente.nombre,cliente.email))
        connection.commit()
        connection.close()
        return {"message": "ACTUALIZADO"}

@app.delete("/clientes/{id_clientes}", response_model=Respuesta)
async def delete_cliente(cliente=Cliente):
    with sqlite3.connect('sql/clientes.sqlite') as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("DELETE FROM clientes WHERE ID = 4",(Cliente.id_clientes))
        connection.commit()
        connection.close()
        return {"message": "ELIMINADO"}
