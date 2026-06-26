from data.pipe import get_stock_data
from strategy.llm import get_strategy_signal
from execution.gatekeeper import validate_trade

def run_pipeline(symbol: str):
    data = get_stock_data(symbol)
    signal = get_strategy_signal(symbol)
    if validate_trade(signal):
        print(f"Trade validated for {symbol}")
        return True
    return False

# Test Integration
if __name__ == "__main__":
    success = run_pipeline("AAPL")
    assert success == True
    print("Integration test passed. Agent ready.")
