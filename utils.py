import os

from dotenv import load_dotenv
from snaptrade_client import SnapTrade

load_dotenv()

user_id = os.getenv("USER_ID")
user_secret = os.getenv("USER_SECRET")
consumer_key = os.getenv("CONSUMER_KEY")
client_id = os.getenv("CLIENT_ID")

client = SnapTrade(client_id=client_id, consumer_key=consumer_key)


def get_snaptrade_client():
    return client


def show_accounts(snaptrade):
    accounts = snaptrade.account_information.list_user_accounts(
        user_id=user_id, user_secret=user_secret
    )
    to_return = []
    for account in accounts.body:
        to_return.append(
            {"account_id": account["id"], "brokerage": account["institution_name"]}
        )
    return to_return


def return_holdings(snaptrade, account_id):
    holdings = snaptrade.account_information.get_user_holdings(
        account_id=account_id, user_id=user_id, user_secret=user_secret
    )
    blahblah = []
    for holding in holdings.body["positions"]:
        blahblah.append(
            {
                "symbol": holding["symbol"]["symbol"]["symbol"],
                "company": holding["symbol"]["symbol"]["description"],
                "currency": holding["symbol"]["symbol"]["currency"]["code"],
                "exchange": holding["symbol"]["symbol"]["exchange"]["code"],
                "figi_code": holding["symbol"]["symbol"]["figi_code"],
                "price": holding["price"],
                "open_pnl": holding["open_pnl"],
                "units": holding["units"],
                "cost_basis": holding["average_purchase_price"],
            }
        )
    return blahblah
