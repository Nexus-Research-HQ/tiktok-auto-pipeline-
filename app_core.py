import sqlite3

class TikTokAppBackendEngine:
    def __init__(self, db_path="tiktok_backend.db"):
        self.db_path = db_path
        self.exchange_rate = 1500.0
        self._init_db()

    def _get_connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_db(self):
        with self._get_connection() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    username TEXT PRIMARY KEY,
                    country TEXT,
                    balance REAL,
                    views INTEGER
                )
            """)
            conn.commit()

    def register_user(self, username: str, country: str):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
            user = cursor.fetchone()

            if user:
                # Return existing user info if already registered
                return {
                    "username": user["username"],
                    "country": user["country"],
                    "balance": user["balance"],
                    "status": "already_registered"
                }

            conn.execute(
                "INSERT INTO users (username, country, balance, views) VALUES (?, ?, ?, ?)",
                (username, country, 20.0, 0)
            )
            conn.commit()

        return {
            "username": username,
            "country": country,
            "balance": 20.0,
            "status": "registered"
        }

    def log_video_view(self, username: str):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
            user = cursor.fetchone()

            if not user:
                # Auto-register if not found for robust testing
                self.register_user(username, "Unknown")
                cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
                user = cursor.fetchone()

            new_views = user["views"] + 1
            new_balance = user["balance"] + 10.0

            conn.execute(
                "UPDATE users SET views = ?, balance = ? WHERE username = ?",
                (new_views, new_balance, username)
            )
            conn.commit()

        return {
            "username": username,
            "views": new_views,
            "new_balance": new_balance
        }

    def process_withdrawal(self, username: str, method: str, destination: str):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
            user = cursor.fetchone()

            if not user:
                raise Exception("User not found")

            balance = user["balance"]
            payout_ngn = balance * self.exchange_rate

            # Reset balance after withdrawal
            conn.execute(
                "UPDATE users SET balance = ? WHERE username = ?",
                (0.0, username)
            )
            conn.commit()

        return {
            "username": username,
            "method": method,
            "destination": destination,
            "payout_ngn": payout_ngn,
            "status": "success"
        }
