import logging

# Configure system logging
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s [%(levelname)s] %(message)s'
)

class TikTokAppBackendEngine:
    def __init__(self, exchange_rate_ngn: float = 1500.0):
        self.users = {}
        self.wallets = {}
        self.exchange_rate = exchange_rate_ngn
        logging.info("TikTok App Backend Engine initialized.")

    def register_user(self, username: str, country: str):
        """Registers a user and assigns referral signup bonuses ($20 for Nigeria, $50 for international)."""
        if username in self.users:
            return {"error": "User already exists"}
        
        bonus = 20.0 if country.lower() == "nigeria" else 50.0
        self.users[username] = {"country": country}
        self.wallets[username] = bonus
        
        logging.info(f"User registered: {username} from {country}. Signup bonus credited: ${bonus}")
        return {"username": username, "balance": self.wallets[username]}

    def log_video_view(self, username: str):
        """Credits $10 to the user wallet when a valid video view milestone is completed."""
        if username not in self.wallets:
            return {"error": "User not found"}
        
        payout = 10.0
        self.wallets[username] += payout
        
        logging.info(f"Video watched by {username}. Credited ${payout}. New balance: ${self.wallets[username]}")
        return {"new_balance": self.wallets[username]}

    def process_withdrawal(self, username: str, method: str, destination: str):
        """Handles currency conversion from USD wallet balances to local bank transfer (Naira) or Gift Card."""
        if username not in self.wallets:
            return {"error": "User not found"}
        
        balance = self.wallets[username]
        if balance <= 0:
            return {"error": "Insufficient balance"}

        if method.lower() == "bank_naira":
            naira_amount = balance * self.exchange_rate
            self.wallets[username] = 0.0
            logging.info(f"Payout processed for {username}: ${balance} converted to ₦{naira_amount:,.2f} sent to bank account: {destination}")
            return {"status": "success", "payout_ngn": naira_amount}

        elif method.lower() == "gift_card":
            self.wallets[username] = 0.0
            logging.info(f"Gift card issued for {username} worth ${balance} sent to {destination}")
            return {"status": "success", "gift_card_value_usd": balance}
        
        else:
            return {"error": "Invalid withdrawal method selected"}

if __name__ == "__main__":
    engine = TikTokAppBackendEngine()
    engine.register_user("daniel_dev", "Nigeria")
    engine.log_video_view("daniel_dev")
    engine.process_withdrawal("daniel_dev", "bank_naira", "Access Bank - 0123456789")
