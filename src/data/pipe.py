import yfinance as yf

def get_stock_data(symbol: str):
    stock = yf.Ticker(symbol)
    return stock.history(period="1d")

# Test
if __name__ == "__main__":
    data = get_stock_data("AAPL")
    assert not data.empty
    print("DataPipe test passed.")
