from fastapi.testclient import TestClient
from code.main import app
clientes = TestClient (app)

def test_index():
    response = clientes.get("/")
    data = {"message" : "Hello World"}
    assert response.status_code == 200
    assert response.json() == data

"""def test_clientes():
    response = clientes.get("/")
    data = ["id_cliente" : 1,
            "nombre" : "Addair",
            "email" : "addair@gmail.com"
            },
            {"id_cliente" : 2,
            "nombre" : "Ignacio",
            "email" : "ignacio@gmail.com"
            },
            {"id_cliente" : 3,
            "nombre" : "Miguel",
            "email" : "miguel@gmail.com"
            }
           ]
    assert response.status_code == 200
    assert response.json() == data
"""

def test_post_cliente():
    payload = {"id_cliente":4,"nombre":"ignacio","email":"addair@email.com"}
    response = clientes.post("/clientes/", json=payload)
    data = {"message":"guardado"}
    assert response.status_code == 200
    assert response.json() == data

def test_put_cliente():
    payload = {
        "id_clientes": 4,
        "nombre":"addair",
        "email":"addair@email.com",
    }
    response = clientes.put("/clientes/", json=payload)
    data = {"message":"actualizado"}
    assert response.status_code == 200
    assert response.json() == data

def test_delete_cliente():
    response = clientes.delete("/clientes/4")
    data = {"message":"eliminado"}
    assert response.status_code == 200
    assert response.json() == data

#4
