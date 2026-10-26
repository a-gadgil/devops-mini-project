def calculate_discount(order_value):
    # Determine the discount rate based on order value
    if order_value > 3000:
        discount_rate = 0.25
    elif 1001 <= order_value <= 3000:
        discount_rate = 0.15
    elif order_value == 1000:
        discount_rate = 0.10
    else:
        discount_rate = 0.0  # 0% discount for orders under 1000

    discount_amount = order_value * discount_rate
    final_price = order_value - discount_amount
    
    return {
        "order_value": order_value,
        "discount_rate": f"{int(discount_rate * 100)}%",
        "discount_amount": discount_amount,
        "final_price": final_price
    }

# --- Example Usage ---
print(calculate_discount(1000))   # 10% discount
print(calculate_discount(2500))   # 15% discount
print(calculate_discount(3500))   # 25% discount