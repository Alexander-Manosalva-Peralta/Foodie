# Foodie_ECommerce_V1.0/services/db_firestore.py

import os
from dotenv import load_dotenv

load_dotenv()

# ===============================
#   MODO FIRESTORE MOCK
# ===============================
USE_MOCK = False
MOCK_MESSAGE_PRINTED = False

def print_mock_message():
    global MOCK_MESSAGE_PRINTED
    if not MOCK_MESSAGE_PRINTED:
        print("🔥 Firestore ejecutándose en MODO MOCK (sin Firebase real)")
        MOCK_MESSAGE_PRINTED = True

# Intentar usar Firebase REAL
try:
    CRED_PATH = os.getenv("FIREBASE_CREDENTIALS_PATH", "")
    PROJECT_ID = os.getenv("FIREBASE_PROJECT_ID", "")

    if CRED_PATH == "mock" or PROJECT_ID == "mock":
        raise Exception("Usando modo mock por variables .env")

    import firebase_admin
    from firebase_admin import credentials, firestore

    if CRED_PATH and os.path.exists(CRED_PATH):
        cred = credentials.Certificate(CRED_PATH)
    else:
        raise Exception("Credenciales no encontradas.")

    firebase_admin.initialize_app(cred, {"projectId": PROJECT_ID})
    db = firestore.client()
    print("✔️ Conexión REAL a Firestore inicializada.")

except Exception as e:
    # Fallback a MOCK
    USE_MOCK = True
    db = None
    print(f"⚠️ Firestore desactivado: {e}")
    print_mock_message()

# ============================================================
#   API COMPATIBLE (Mock vs Real)
# ============================================================

def get_db():
    """Devuelve Firestore real o lanza error si es real y no funciona."""
    if USE_MOCK:
        print_mock_message()
        raise Exception("Firestore está en modo MOCK. No existe conexión real.")
    return db

def mock_save_order(order_data):
    """Simula guardar una orden sin Firestore."""
    print_mock_message()
    print("📝 Orden guardada (MOCK):", order_data)
    return "MOCK_ORDER_ID_12345"

def save_order(order_data: dict) -> str:
    """Guarda una orden (real o mock)."""
    if USE_MOCK:
        return mock_save_order(order_data)

    try:
        db = get_db()
        doc_ref = db.collection('orders').document()
        doc_ref.set(order_data)
        return doc_ref.id
    except Exception as e:
        print(f"Error real al guardar la orden: {e}")
        return mock_save_order(order_data)
