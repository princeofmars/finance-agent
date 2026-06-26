import alpaca_trade_api as tradeapi
import os

API_KEY = os.getenv("ALPACA_API_KEY", "DEMO_KEY")
API_SECRET = os.getenv("ALPACA_SECRET", "DEMO_SECRET")
BASE_URL = "https://paper-api.alpaca.markets"

api = tradeapi.REST(API_KEY, API_SECRET, BASE_URL, api_version='v2')

def execute_order(symbol: str, qty: int, side: str):
    try:
        api.submit_order(
            symbol=symbol,
            qty=qty,
            side=side,
            type='market',
            time_in_force='gtc'
        )
        return True
    except Exception as e:
        print(f"Trade failed: {e}")
        return False
