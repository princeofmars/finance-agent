from http.server import BaseHTTPRequestHandler
import json
import sys
import os

# Ensure the src directory is in the path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from data.pipe import get_stock_data
from strategy.llm import get_strategy_signal
from execution.gatekeeper import validate_trade

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        symbol = "AAPL" # Defaulting for demonstration
        data = get_stock_data(symbol)
        signal = get_strategy_signal(symbol)
        is_valid = validate_trade(signal)
        
        response = {
            "symbol": symbol,
            "status": "Validated" if is_valid else "Rejected",
            "signal": signal
        }
        
        self.wfile.write(json.dumps(response).encode())
        return
