from fastapi import FastAPI
import asyncio

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