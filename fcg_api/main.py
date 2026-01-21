app = FastAPI(
    title="FGC API",
    description="API for managing power converter devices",
    version="1.0.0"
)

@app.get("/health")
def health_check():
    return {"status": "ok"}