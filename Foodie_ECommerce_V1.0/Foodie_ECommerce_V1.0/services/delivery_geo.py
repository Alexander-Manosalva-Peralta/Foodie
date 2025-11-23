# Delivery zone and fee calculations
def calculate_fee(distance_km):
    base = 300  # cents
    per_km = 100
    return base + int(distance_km * per_km)
