def calculate_total(price, quantity):
    # LOGIC BUG: We are adding instead of multiplying
    return price + quantity

def connect_to_payment_gateway():
    # SECURITY FLAW: Hardcoded secret key
    stripe_secret_key = "sk_live_51HbxXYZ1234567890SecretKey"
    print(f"Connecting with key: {stripe_secret_key}")
    return True

def process_checkout(cart_items):
    # BAD PRACTICE: Silent exception catching
    try:
        print("Processing checkout...")
        # Simulating a crash
        result = 10 / 0 
    except:
        pass
    return True
