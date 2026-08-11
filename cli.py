import argparse
import sys
from app_core import TikTokAppBackendEngine

def main():
    parser = argparse.ArgumentParser(description="TikTok Automation Backend CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Register command
    parser_reg = subparsers.add_parser("register", help="Register a new user")
    parser_reg.add_argument("username", type=str, help="Username of the user")
    parser_reg.add_argument("country", type=str, help="Country of the user")

    # View command
    parser_view = subparsers.add_parser("view", help="Simulate watching a video and earning credits")
    parser_view.add_argument("username", type=str, help="Username of the viewer")

    # Withdraw command
    parser_withdraw = subparsers.add_parser("withdraw", help="Process a payout for a user")
    parser_withdraw.add_argument("username", type=str, help="Username requesting withdrawal")
    parser_withdraw.add_argument("method", type=str, help="Payout method (e.g., bank_naira)")
    parser_withdraw.add_argument("destination", type=str, help="Bank account or destination info")

    args = parser.parse_args()
    engine = TikTokAppBackendEngine()

    try:
        if args.command == "register":
            result = engine.register_user(args.username, args.country)
            print("\n[SUCCESS] User Registered:")
            for k, v in result.items():
                print(f"  {k}: {v}")

        elif args.command == "view":
            result = engine.log_video_view(args.username)
            print("\n[SUCCESS] Video View Logged:")
            for k, v in result.items():
                print(f"  {k}: {v}")

        elif args.command == "withdraw":
            result = engine.process_withdrawal(args.username, args.method, args.destination)
            print("\n[SUCCESS] Withdrawal Processed:")
            for k, v in result.items():
                print(f"  {k}: {v}")

    except Exception as e:
        print(f"\n[ERROR] {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
