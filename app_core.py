class TikTokAppBackendEngine:
    def __init__(self):
        self.exchange_rate = 1500.0
        self.users = {}

    def register_user(self, username: str, country: str):
        self.users[username] = {
            "country": country,
            "balance": 20.0,
            "views": 0
        }
        return {
            "username": username,
            "country": country,
            "balance": 20.0,
            "status": "registered"
        }

    def log_video_view(self, username: str):
        if username not in self.users:
            # Auto-register if not found for robust testing
            self.register_user(username, "Unknown")
        
        self.users[username]["views"] += 1
        self.users[username]["balance"] += 10.0
        
        return {
            "username": username,
            "views": self.users[username]["views"],
            "new_balance": self.users[username]["balance"]
        }

    def process_withdrawal(self, username: str, method: str, destination: str):
        if username not in self.users:
            raise Exception("User not found")
        
        balance = self.users[username]["balance"]
        payout_ngn = balance * self.exchange_rate
        
        # Reset balance after withdrawal
        self.users[username]["balance"] = 0.0

        return {
            "username": username,
            "method": method,
            "destination": destination,
            "payout_ngn": payout_ngn,
            "status": "success"
        }
