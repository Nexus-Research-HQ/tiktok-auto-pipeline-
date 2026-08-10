# TikTok Auto Pipeline & Payout Backend

An automated backend engine and API server designed to manage user wallets, track video view milestones, and process multi-tier payouts (local signups, international signups, and automated bank/gift card withdrawals).

## Project Structure
* `app_core.py`: Core ledger and payout math engine.
* `api_server.py`: FastAPI endpoints for registration, views, and withdrawals.
* `test_app.py`: Automated verification script for the backend workflow.
* `ARCHITECTURE.md`: Detailed specification of system rules and monetization tiers.

## Installation & Setup
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   uvicorn api_server:app --reload
   
