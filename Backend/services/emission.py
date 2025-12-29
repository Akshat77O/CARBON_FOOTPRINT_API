import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "emission_factors.json")

with open(DATA_PATH, "r") as f:
    EMISSION_FACTORS = json.load(f)

def calculate_transport_emission(weight, quantity, distance, transport_mode):
    factor = EMISSION_FACTORS.get(transport_mode, 0.15)
    weight_in_tons = (weight * quantity) / 1000
    return weight_in_tons * distance * factor
