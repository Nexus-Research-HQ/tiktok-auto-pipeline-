# TikTok Payout App Architecture

## Monetization & Payout Rules
* **Video Views:** Credits **$10.00 USD** to the user wallet per valid video view milestone.
* **Local Signups (Nigeria):** Credits a **$20.00 USD** signup/download bonus.
* **International Signups (Abroad):** Credits a **$50.00 USD** signup/download bonus.

## Withdrawal & Off-ramp Options
* **Local Bank Payout (Naira):** Automatically converts USD wallet balances into Nigerian Naira (NGN) via live exchange rates for direct bank transfers.
* **Gift Cards:** Allows users to redeem their USD wallet balance directly for digital gift cards.

## Backend Components
* `app_core.py`: Manages user accounts, wallet ledgers, view tracking, and payout conversion math.
* `api_server.py`: Exposes FastAPI endpoints for registration, video view tracking, and withdrawal requests.
