# Foodie_ECommerce_V1.0/services/db_firestore.py

import firebase_admin
from firebase_admin import credentials, firestore
import os
from dotenv import load_dotenv

# Carga variables de entorno para configuración
load_dotenv()

# Inicialización de Firebase (se realiza una sola vez)
try:
    # Usar credenciales de archivo o variables de entorno
    cred_path = os.environ.get('FIREBASE_CREDENTIALS_PATH')
    if cred_path and os.path.exists(cred_path):
        cred = credentials.Certificate(cred_path)
    else:
        # Fallback para usar variables de entorno si el path no existe
        print("Advertencia: Usando credenciales de entorno para Firebase. Asegúrate de configurar FIREBASE_PROJECT_ID.")
        cred = credentials.ApplicationDefault()

    firebase_admin.initialize_app(cred, {
        'projectId': os.environ.get('FIREBASE_PROJECT_ID'),
    })
    db = firestore.client()
    print("Conexión a Firestore inicializada.")
except Exception as e:
    db = None
    print(f"Error al inicializar Firebase/Firestore: {e}")

def get_db():
    """Retorna la instancia del cliente Firestore."""
    if not db:
        raise Exception("Firestore no está inicializado. Revisa tus credenciales.")
    return db

def save_order(order_data: dict) -> str:
    """Guarda una nueva orden en la colección 'orders'."""
    try:
        db = get_db()
        # Firestore autogenera el ID si no se especifica uno
        doc_ref = db.collection('orders').document()
        doc_ref.set(order_data)
        return doc_ref.id
    except Exception as e:
        print(f"Error al guardar la orden en Firestore: {e}")
        raise