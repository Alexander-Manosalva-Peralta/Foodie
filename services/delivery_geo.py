# Foodie_ECommerce_V1.0/services/delivery_geo.py

import random


# --- MOCK/SIMULACIÓN DEL SERVICIO DE GEOLOCALIZACIÓN ---

def calculate_delivery_cost(zip_code: str) -> float:
    """
    Simula el cálculo del costo de envío basado en el código postal o zona.
    En un entorno real, usaría una API como Google Maps Distance Matrix.
    """
    print(f"Calculando costo de envío para código postal: {zip_code}...")

    # Lógica de zonas de ejemplo
    if zip_code.startswith('15'):  # Lima Norte (Ejemplo)
        cost = 15.00
    elif zip_code.startswith('18'):  # Miraflores/San Isidro (Ejemplo)
        cost = 10.00
    elif zip_code.startswith('00'):  # Error/Zona no cubierta
        raise Exception("El código postal no pertenece a nuestra zona de cobertura.")
    else:
        # Costo por defecto o cálculo más complejo
        cost = 12.50 + (random.randint(0, 50) / 100)  # Añade un poco de variación

    return cost


def check_service_area(latitude: float, longitude: float) -> bool:
    """Simula la verificación si la dirección está dentro del área de servicio."""
    # En un proyecto real, se verificaría contra un polígono geográfico
    return True  # Siempre disponible en el mock