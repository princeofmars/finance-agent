import os

def get_strategy_signal(symbol: str):
    # This represents the LLM logic
    # In production, this would call your LLM provider
    return {"symbol": symbol, "size": 100, "action": "buy"}

# Test
if __name__ == "__main__":
    signal = get_strategy_signal("AAPL")
    assert signal["action"] == "buy"
    print("Strategy test passed.")
