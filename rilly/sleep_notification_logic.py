from datetime import datetime, timedelta

def check_wind_down_nudge(user_sleep_time_str: str) -> dict:
    """
    Checks if it is time to send the 30-minute wind-down nudge.
    
    :param user_sleep_time_str: User's set sleep time in "HH:MM" 24-hour format (e.g., "22:30")
    :dict Returns action status, message, and target trigger time.
    """
    now = datetime.now()
    
    # Parse the user's sleep time
    sleep_time_obj = datetime.strptime(user_sleep_time_str, "%H:%M").time()
    
    # Combine today's date with the user's sleep time
    sleep_datetime = datetime.combine(now.date(), sleep_time_obj)
    
    # Calculate the exact time to trigger the 30-minute nudge
    nudge_time = sleep_datetime - timedelta(minutes=30)
    
    # Check if current time is at or past the nudge time, but before sleep time
    time_difference = (nudge_time - now).total_seconds()
    
    if -60 <= time_difference <= 0: # 1-minute window check to prevent missing exact triggers
        return {
            "should_nudge": True,
            "message": "Time to wind down! Your bedtime is in 30 minutes.",
            "trigger_time": nudge_time.strftime("%H:%M")
        }
    
    return {
        "should_nudge": False,
        "current_time": now.strftime("%H:%M"),
        "scheduled_nudge_time": nudge_time.strftime("%H:%M")
    }

# --- Example Usage ---
# Assuming the user set their sleep time to 11:00 PM (23:00)
result = check_wind_down_nudge("23:00")
print(result)