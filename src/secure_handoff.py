"""Secure delivery OTP verification module."""

import secrets
import time


class SecureDeliveryVerification:
    """Handles secure delivery OTP generation and verification."""

    def __init__(self, expiry_seconds: int = 300) -> None:
        self.active_deliveries = {}
        self.expiry_duration = expiry_seconds

    def trigger_delivery_otp(
        self, order_id: str, is_at_location: bool, agent_confirmed: bool
    ) -> str:
        """Generate a 6-digit secure OTP upon agent arrival."""
        if not (is_at_location and agent_confirmed):
            raise PermissionError(
                "Conditions not met: Agent must confirm arrival."
            )

        otp = "".join(str(secrets.randbelow(10)) for _ in range(6))
        expires_at = time.time() + self.expiry_duration

        self.active_deliveries[order_id] = {
            "otp": otp,
            "expires_at": expires_at,
            "verified": False,
        }

        print(
            f"[SMS Service] Sending OTP {otp} to customer for "
            f"Order {order_id}"
        )
        return otp

    def verify_delivery_otp(self, order_id: str, entered_otp: str) -> bool:
        """Verify the OTP entered during handoff."""
        if order_id not in self.active_deliveries:
            print("Error: No active delivery session found.")
            return False

        delivery_record = self.active_deliveries[order_id]

        if delivery_record["verified"]:
            print("Error: OTP has already been used.")
            return False

        if time.time() > delivery_record["expires_at"]:
            print("Error: OTP has expired.")
            return False

        if delivery_record["otp"] == entered_otp:
            delivery_record["verified"] = True
            print("Success: Delivery verified successfully!")
            return True

        print("Error: Invalid OTP entered.")
        return False


if __name__ == "__main__":
    verifier = SecureDeliveryVerification()
    order = "ORDER_BLNK_98765"

    delivery_arrived = True
    agent_checked_in = True

    try:
        generated_otp = verifier.trigger_delivery_otp(
            order, delivery_arrived, agent_checked_in
        )
        verifier.verify_delivery_otp(order, "000000")
        verifier.verify_delivery_otp(order, generated_otp)
    except Exception as e:
        print(e)