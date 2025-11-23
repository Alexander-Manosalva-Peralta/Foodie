# Foodie_ECommerce_V1.0/services/payment_processor.py

import time
import random


# --- MOCK/SIMULACIÓN DEL PROCESADOR DE PAGOS (Niubiz/Mercado Pago) ---

def process_payment_mock(amount: float, token: str) -> dict:
    """
    Simula la llamada a la API de un procesador de pagos (e.g., Niubiz, MP).
    En un entorno real, esto sería una solicitud HTTP POST.
    """
    print(f"Procesando pago simulado por ${amount} con token: {token}...")
    time.sleep(1)  # Simula latencia de red

    # Simula una falla si el token es "FAIL"
    if token.upper() == 'FAIL':
        return {
            'status': 'failed',
            'error': 'Token de prueba fallido simulado.',
            'transaction_id': None
        }

    # Simulación de transacción exitosa
    transaction_id = f"TID-{int(time.time())}-{random.randint(1000, 9999)}"
    return {
        'status': 'success',
        'transaction_id': transaction_id,
        'amount': amount,
        'timestamp': time.strftime("%Y-%m-%d %H:%M:%S")
    }