from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import clientes, equipos, ordenes
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# Servir archivos estáticos (CSS, JS, imágenes, etc.)
app.mount("/static", StaticFiles(directory="frontend"), name="static")

# Servir el index.html al acceder a la raíz
@app.get("/")
def get_index():
    return FileResponse(os.path.join("frontend", "index.html"))


# Middleware de logging para debugging
@app.middleware("http")
async def logging_middleware(request, call_next):
    print(f"Request Method: {request.method}")
    print(f"Request URL: {request.url}")
    print(f"Request Headers: {request.headers}")
    response = await call_next(request)
    print(f"Response Status: {response.status_code}")
    return response

# Configurar CORS
origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
    "http://127.0.0.1:8000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization", "Accept"],
    max_age=3600,
)

app.include_router(clientes.router, prefix="/api")
app.include_router(equipos.router, prefix="/api")
app.include_router(ordenes.router, prefix="/api")


## realizamos cambios para probar la rama..