from pydantic import BaseModel, Field

class DeviceConfig(BaseModel):
    voltage: float = Field(..., gt=0)
    current: float = Field(..., gt=0)
    enabled: bool = True