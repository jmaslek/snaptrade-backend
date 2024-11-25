# OpenBB SnapTrade Backend

![1730305473514](https://github.com/user-attachments/assets/f847257e-94ea-496d-ae4f-d99f9d4b52be)


This example backend integrates with [SnapTrade](https://snaptrade.com/) for pulling in your portfolio holdings.

### Prerequisites

This assumes that you have already gone through the account setup and you have the following

- CONSUMER_KEY
- CLIENT_ID
- USER_ID
- USER_SECRET

These should be defined in `.env`.  We have provided a sample, which you can run
```bash
cp .env.example .env 
```
And then edit directly

If you have not set up your accounts, you should do so at: **https://docs.snaptrade.com/demo/getting-started**.  It is very simple.

### Running this custom backend

After cloning the repo, just setup your venv and we are pretty much done
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m uvicorn main:app --host 0.0.0.0 --port 8000
```

This will spin up a FastAPI running on http://0.0.0.0:8000

This backend can then be plugged into your OpenBB Terminal account.

### Current Widgets
- List Accounts
  - Shows what accounts you have connected.  Returns an account_id to be used for:
- Holdings
  - Requires the input to be an account_id from the previous widget.  Will return the equity holdings from that account.
