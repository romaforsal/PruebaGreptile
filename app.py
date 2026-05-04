import os # Necesario para usar variables de entorno

def calculate_total(price, quantity):
    # FIXED: Back to multiplication
    return price * quantity

def connect_to_payment_gateway():
    # FIXED: Never hardcode secrets. In a real app, use environment variables.
    # stripe_secret_key = os.environ.get("STRIPE_SECRET_KEY") 
    print("Connecting using secure configuration...")
    return True

def process_checkout(cart_items):
    # FIXED: Specific exception catching and logging
    try:
        print("Processing checkout...")
        result = 10 / 0
        return True
    except ZeroDivisionError as e:
        print(f"Error processing checkout: Division by zero - {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False
