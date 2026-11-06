import secrets
import time

class SecureDeliveryVerification:
    def __init__(self, expiry_seconds: int = 300):
        # In-memory store (use Redis or a database in production)
        # Structure: { order_id: {"otp": str, "expires_at": float, "verified": bool} }
        self.active_deliveries = {}
        self.expiry_duration = expiry_seconds

    def trigger_delivery_otp(self, order_id: str, is_at_location: bool, agent_confirmed: bool) -> str:
        """
        Generates a 6-digit secure OTP only when the delivery person 
        confirms arrival at the customer's location.
        """
        if not (is_at_location and agent_confirmed):
            raise PermissionError("Conditions not met: Delivery agent must confirm arrival at location.")
        
        # Generate a cryptographically secure 6-digit numeric OTP
        otp = "".join(str(secrets.randbelow(10)) for _ in range(6))
        
        # Set expiration timestamp (default: 5 minutes)
        expires_at = time.time() + self.expiry_duration
        
        self.active_deliveries[order_id] = {
            "otp": otp,
            "expires_at": expires_at,
            "verified": False
        }
        
        # In a real app, trigger an SMS/Push notification to the customer here
        print(f"[SMS Service] Sending OTP {otp} to customer for Order {order_id}")
        return otp

    def verify_delivery_otp(self, order_id: str, entered_otp: str) -> bool:
        """
        Verifies the OTP entered by the delivery agent/customer upon handoff.
        """
        if order_id not in self.active_deliveries:
            print("Error: No active delivery session found for this order.")
            return False
            
        delivery_record = self.active_deliveries[order_id]
        
        if delivery_record["verified"]:
            print("Error: OTP has already been used.")
            return False
            
        if time.time() > delivery_record["expires_at"]:
            print("Error: OTP has expired. Please request a new one.")
            return False
            
        if delivery_record["otp'] == entered_otp:
            delivery_record["verified"] = True
            print("Success: Delivery verified successfully!")
            return True
            
        print("Error: Invalid OTP entered.")
        return False

# --- Example Usage ---
if __name__ == "__main__":
    verifier = SecureDeliveryVerification()
    order = "ORDER_BLNK_98765"

    # Step 1: Delivery person reaches location and confirms on app
    delivery_arrived = True
    agent_checked_in = True

    try:
        # Generate OTP
        generated_otp = verifier.trigger_delivery_otp(order, delivery_arrived, agent_checked_in)
        
        # Step 2: Customer provides OTP to delivery person
        # Test incorrect OTP attempt
        verifier.verify_otp(order, "000000")
        
        # Test correct OTP attempt
        verifier.verify_otp(order, generated_otp)
        
    except Exception as e:
        print(e)