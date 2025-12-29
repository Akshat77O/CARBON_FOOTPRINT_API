from pydantic import BaseModel

class CarbonRequest(BaseModel):
    weight: float
    quantity: int
    origin_zip: str
    destination_zip: str
    transport_mode: str
    packaging: str
