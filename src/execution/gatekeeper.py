import pydantic
from typing import Dict

class RiskParams(pydantic.BaseModel):
    max_position_size: float = 1000.0
    allowed_symbols: list = ["AAPL", "TSLA", "MSFT"]

def validate_trade(signal: Dict):
    params = RiskParams()
    if signal["symbol"] not in params.allowed_symbols:
        raise ValueError("Symbol not allowed")
    if signal["size"] > params.max_position_size:
        raise ValueError("Position size exceeds risk limit")
    return True

# Test
if __name__ == "__main__":
    test_signal = {"symbol": "AAPL", "size": 500}
    assert validate_trade(test_signal) == True
    print("Gatekeeper test passed.")
