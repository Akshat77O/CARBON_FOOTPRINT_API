from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from models import CarbonRequest
from services.distance import get_distance
from services.emission import calculate_transport_emission
from services.packaging import get_packaging_emission

app = FastAPI(title="Carbon Footprint API")

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Carbon Footprint API is running"}


@app.post("/api/calculate")
def calculate_carbon(data: CarbonRequest):
    try:
        distance = get_distance(data.origin_zip, data.destination_zip)

        transport_emission = calculate_transport_emission(
            data.weight,
            data.quantity,
            distance,
            data.transport_mode
        )

        packaging_emission = get_packaging_emission(data.packaging)

        total_emission = round(transport_emission + packaging_emission, 2)

        eco_score = "A" if total_emission < 0.5 else "B" if total_emission < 1 else "C"

        return {
            "carbon_kg": total_emission,
            "distance_km": round(distance, 2),
            "transport_mode": data.transport_mode,
            "eco_score": eco_score
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
