def check_rilly_reward(total_steps: int, total_days: int) -> str:
    """
    Checks if a Rilly user qualifies for the step challenge reward.
    
    Args:
        total_steps (int): Total steps recorded by the user.
        total_days (int): Total days tracked in the challenge period.
        
    Returns:
        str: Message indicating reward status or progress.
    """
    REQUIRED_STEPS = 1_800_000
    REQUIRED_DAYS = 180
    REWARD_COINS = 25_000
    
    if total_days >= REQUIRED_DAYS and total_steps >= REQUIRED_STEPS:
        return f"Congratulations! You've unlocked {REWARD_COINS:,} Rilly Coins!"
    else:
        steps_needed = max(0, REQUIRED_STEPS - total_steps)
        days_remaining = max(0, REQUIRED_DAYS - total_days)
        return (
            f"Keep moving! You need {steps_needed:,} more steps "
            f"across {days_remaining} remaining days to earn your {REWARD_COINS:,} Rilly Coins."
        )

# Example Usage:
user_steps = 1_850_000
user_days = 180

print(check_rilly_reward(user_steps, user_days))