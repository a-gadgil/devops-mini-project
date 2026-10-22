from datetime import datetime, timedelta


def can_post_free_ad(last_free_ad_timestamp):
    """
    Checks if a user is eligible for a free ad based on a 60-day cooldown.

    Args:
        last_free_ad_timestamp (datetime or None): The timestamp of the user's last free ad.

    Returns:
        bool: True if allowed to post a free ad, False if they must buy a paid ad.
    """
    if last_free_ad_timestamp is None:
        return True  # User has never posted a free ad

    cooldown = timedelta(days=60)
    time_elapsed = datetime.now() - last_free_ad_timestamp

    return time_elapsed >= cooldown


# --- Example Usage ---
if __name__ == "__main__":
    # Case 1: User posted 30 days ago (Should be blocked)
    recent_ad = datetime.now() - timedelta(days=30)
    print("Posted 30 days ago - Can post free ad?", can_post_free_ad(recent_ad))

    # Case 2: User posted 65 days ago (Should be allowed)
    old_ad = datetime.now() - timedelta(days=65)
    print("Posted 65 days ago - Can post free ad?", can_post_free_ad(old_ad))
