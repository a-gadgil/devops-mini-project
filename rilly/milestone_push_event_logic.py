class RillyNotificationService:
    @staticmethod
    def send_push_notification(user_id: str, title: str, body: str):
        """Mock push notification gateway."""
        print(f"  [PUSH NOTIFICATION -> User {user_id}] {title}: {body}")


class RillyStepTracker:
    def __init__(self, user_id: str, daily_target: int = 10000, milestone_step: int = 2500):
        self.user_id = user_id
        self.daily_target = daily_target
        self.milestone_step = milestone_step
        
        # State tracking for the current day
        self.current_steps = 0
        self.last_notified_milestone = 0
        self.target_reached_notified = False

    def log_steps(self, steps_walked: int):
        """
        Updates total steps walked and checks if a new 2500-step milestone 
        has been unlocked.
        """
        if steps_walked <= 0:
            return

        self.current_steps += steps_walked
        print(f"\n[Activity Synced] +{steps_walked:,} steps added. Total today: {self.current_steps:,} / {self.daily_target:,}")

        # Calculate which milestone tier the user is currently at (e.g., 2500, 5000, 7500, 10000)
        current_milestone = (self.current_steps // self.milestone_step) * self.milestone_step
        
        # Cap the milestone check at the daily target
        if current_milosphere_capped := min(current_milestone, self.daily_target):
            
            # If the user has crossed a new milestone boundary that we haven't notified yet
            if current_milosphere_capped > self.last_notified_milestone:
                self._trigger_milestone_notification(current_milosphere_capped)
                self.last_notified_milestone = current_milosphere_capped

    def _trigger_milestone_notification(self, milestone: int):
        """Sends contextual push notification depending on the milestone tier."""
        if milestone < self.daily_target:
            percentage = int((milestone / self.daily_target) * 100)
            title = f"🎯 {milestone:,} Steps Completed! ({percentage}%)"
            body = "Great pace! Keep moving to crush your daily Rilly goal."
        else:
            title = "🏆 Daily Goal Achieved!"
            body = "Amazing job! You've hit your 10,000 steps target for today."

        RillyNotificationService.send_push_notification(self.user_id, title, body)

    def reset_daily_progress(self):
        """Resets tracking counters at midnight for a new day."""
        self.current_steps = 0
        self.last_notified_milestone = 0
        self.target_reached_notified = False
        print("\n[System] Daily step counters reset for a new day.")


# --- Demo / Testing the Milestone Logic ---
if __name__ == "__main__":
    # Initialize tracker for user 'aditya'
    tracker = RillyStepTracker(user_id="usr_aditya", daily_target=10000, milestone_step=2500)

    print("--- Simulating User Walking Throughout the Day ---")
    
    # User goes for a morning walk
    tracker.log_steps(1200)   # No milestone crossed yet
    tracker.log_steps(1400)   # Total: 2,600 -> Crosses 2,500 milestone (1st Notification)
    
    # User goes about afternoon chores
    tracker.log_steps(2200)   # Total: 4,800 -> Still under 5,000
    tracker.log_steps(300)    # Total: 5,100 -> Crosses 5,000 milestone (2nd Notification)
    
    # User goes for an evening jog
    tracker.log_steps(3000)   # Total: 8,100 -> Crosses 7,500 milestone (3rd Notification)
    
    # User completes final steps before bed
    tracker.log_steps(2000)   # Total: 10,100 -> Crosses 10,000 milestone (4th & Final Notification)
    
    # Extra steps walked after target completion (should not spam duplicate notifications)
    tracker.log_steps(1500)   # Total: 11,600 -> Already capped at target milestone