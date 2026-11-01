import time

class OrderManager:
    def __init__(self, order_id, initial_items):
        self.order_id = order_id
        self.items = list(initial_items)
        self.created_at = time.time()  # Record the exact order placement timestamp
        self.window_limit = 45          # 45-second window

    def add_product(self, product_name):
        current_time = time.time()
        elapsed_time = current_time - self.created_at

        # Check if within the 45-second window
        if elapsed_time <= self.window_limit:
            self.items.append(product_name)
            remaining_time = int(self.window_limit - elapsed_time)
            print(f"✅ Success! Added '{product_name}' to Order #{self.order_id}.")
            print(f"   ({remaining_time} seconds remaining in the edit window.)")
            return True
        else:
            print(f"❌ Could not add '{product_name}'. The 45-second modification window has expired.")
            return False

# --- Example Usage ---
if __name__ == "__main__":
    # 1. Order is placed successfully
    my_order = OrderManager(order_id="ORD-5092", initial_items=["Pizza", "Coke"])
    print(f"Order placed with items: {my_order.items}\n")

    # 2. User tries adding an item immediately (within window)
    my_order.add_product("Garlic Bread")

    # 3. Simulate user waiting for longer than 45 seconds
    print("\n⏳ Simulating time passing (waiting 46 seconds)...")
    my_order.created_at -= 46  # Backdate the timestamp to simulate expiration

    # 4. User tries adding another item after the window closes
    my_order.add_product("Extra Napkins")
