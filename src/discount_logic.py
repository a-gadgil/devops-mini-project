def check_makemytrip_reward(monthly_spend):
    """
    Determines if a customer qualifies for a Rs 500 MakeMyTrip coupon
    based on their total monthly shopping amount (> 15000 Rs).
    """
    THRESHOLD = 15000
    COUPON_VALUE = 500

    if monthly_spend > THRESHOLD:
        return {
            "qualified": True,
            "monthly_spend": monthly_spend,
            "reward": f"MakeMyTrip Rs {COUPON_VALUE} Coupon",
            "message": f"Congratulations! You unlocked a Rs {COUPON_VALUE} MakeMyTrip coupon."
        }
    else:
        shortfall = THRESHOLD - monthly_spend
        return {
            "qualified": False,
            "monthly_spend": monthly_spend,
            "amount_needed": shortfall,
            "message": f"Spend Rs {shortfall} more this month to unlock your MakeMyTrip coupon."
        }


# --- Example Usage ---
# Customer hasn't reached the threshold yet
print(check_makemytrip_reward(12000))
print(check_makemytrip_reward(17500))  # Customer qualifies
