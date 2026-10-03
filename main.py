from fastapi import FastAPI

app = FastAPI(title="Simple FastAPI App")

@app.get("/")
def read_root():
    return {"message": "¡Hola! La API con FastAPI está funcionando correctamente."}

@app.get("/get")
def get_data():
    return {
        "status": "success",
        "message": "Respuesta exitosa desde el endpoint /get",
        "data": {
            "usuario": "ejemplo",
            "estado": "activo"
        }
    }
