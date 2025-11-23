# Payment processor abstraction (Niubiz/Mercado Pago)
class PaymentProcessor:
    def __init__(self, provider="niubiz", api_key=None):
        self.provider = provider
        self.api_key = api_key

    def create_payment(self, amount_cents, currency="PEN", **kwargs):
        # Implement provider-specific calls
        raise NotImplementedError
