from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FGC API"
    debug: bool = False

settings = Settings()