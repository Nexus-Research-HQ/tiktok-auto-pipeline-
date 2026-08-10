from app_core import TikTokAppBackendEngine

def test_backend_workflow():
    engine = TikTokAppBackendEngine()

    # 1. Register a test user from Nigeria
    reg = engine.register_user("test_user_ng", "Nigeria")
    print("Registration:", reg)

    # 2. Simulate watching a video
    view_res = engine.log_video_view("test_user_ng")
    print("Video View Credit:", view_res)

    # 3. Request a local bank payout
    payout = engine.process_withdrawal("test_user_ng", "bank_naira", "1234567890")
    print("Payout Result:", payout)

if __name__ == "__main__":
    test_backend_workflow()
