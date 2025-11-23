# Foodie_ECommerce_V1.0/services/notification_manager.py

# NOTA: En un entorno real se usaría:
# - Email: SendGrid, Mailgun, AWS SES
# - SMS/WhatsApp: Twilio, Infobip

def send_email(to_email: str, subject: str, body_html: str):
    """Simula el envío de un correo electrónico de confirmación."""
    print(f"--- EMAIL SIMULADO ---")
    print(f"PARA: {to_email}")
    print(f"ASUNTO: {subject}")
    print(f"CUERPO: ... contenido HTML ...")
    print(f"----------------------")

def send_confirmation_email(order: dict):
    """Envía la confirmación de la orden."""
    subject = f"Confirmación de Orden #{order.get('id')}"
    body = f"""
    <h1>¡Gracias por tu compra, {order.get('user_id')}!</h1>
    <p>Tu orden por un total de {order.get('total_amount')} ha sido confirmada.</p>
    <p>La orden será enviada a: {order.get('shipping_address', {}).get('street')}</p>
    """
    send_email(
        to_email=order.get('user_email', 'cliente@ejemplo.com'),
        subject=subject,
        body_html=body
    )

def send_sms_notification(to_phone: str, message: str):
    """Simula el envío de un SMS."""
    print(f"--- SMS SIMULADO ---")
    print(f"PARA: {to_phone}")
    print(f"MENSAJE: {message}")
    print(f"--------------------")