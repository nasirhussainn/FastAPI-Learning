from fastapi import FastAPI
import asyncio
from fastapi import HTTPException, Depends
from .models.schema import DeviceConfig
from .core.config import settings
from .core.db import get_db

app = FastAPI(
    title="FGC API",
    description="API for managing power converter devices",
    version="1.0.0"
)

@app.get("/health")
# The function is sync, so FastAPI runs it in a threadpool
# def health_check(): 
#     return {"status": "ok"}

async def health_check():
    await asyncio.sleep(5)
    return {"status": "ok"}


# device_id: int → automatic validation
# Invalid input → 422 Unprocessable Entity
# No manual parsing needed
# @app.get("/devices/{device_id}")
# def get_device(
#     device_id: int,
#     include_config: bool = False
# ):
#     if device_id <= 0:
#         raise HTTPException(status_code=400, detail="Invalid device ID")

#     return {
#         "device_id": device_id,
#         "include_config": include_config
#     }

@app.post("/devices/{device_id}/config")
def update_config(device_id: int, config: DeviceConfig):
    return {
        "device_id": device_id,
        "config": config
    }
    
@app.get("/devices/{device_id}", response_model=DeviceConfig)
def get_device(device_id: int):
    return {
        "voltage": 1.3333,
        "current": 1,
        "enabled": True
    }
    
def get_settings():
    return settings

# Depends() tells FastAPI to resolve the dependency
# Settings are injected per request
# No global coupling inside endpoint logic
@app.get("/info")
def app_info(settings=Depends(get_settings)):
    return {
        "app": settings.app_name,
        "debug": settings.debug
    }

# “Using dependencies instead of globals allows configuration to be overridden 
# in tests and keeps the endpoint logic decoupled from environment concerns.”
# @app.get("/info")
# def app_info():
#     return {"app": settings.app_name}


# “Database sessions must be request-scoped. Sharing sessions across concurrent 
# requests can corrupt transactions.”
# One DB session per request
# Proper cleanup
# Thread-safe
@app.get("/list_device")
def list_devices(db=Depends(get_db)):
    return db.execute("SELECT * FROM devices").fetchall()


# Shared DB session across requests
# Race conditions
# Connection leaks
# db = SessionLocal()
# @app.get("/devices")
# def list_devices():
#     return db.execute("SELECT * FROM devices")

