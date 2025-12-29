PACKAGING_EMISSION = {
    "cardboard": 0.05,
    "plastic": 0.12,
    "eco": 0.01
}

def get_packaging_emission(packaging):
    return PACKAGING_EMISSION.get(packaging.lower(), 0.05)
