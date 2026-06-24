# Aquí pongo las variables del sistema
import os
from dotenv import load_dotenv

load_dotenv()

TIMEFRAME = "4H"  #Timeframe for data analysis (e.g., "1H", "4H", "1D")

VALOR_EMA_RAPIDA = 12
VALOR_EMA_LENTA = 26

# Alpaca
ALPACA_TRADING_ENDPOINT = "https://paper-api.alpaca.markets/v2"
ALPACA_DATA_ENDPOINT = "https://data.alpaca.markets/v2"
ALPACA_API_KEY = os.getenv("ALPACA_API_KEY")
ALPACA_API_SECRET = os.getenv("ALPACA_API_SECRET")

TICKER_YAHOO = "TSLA"  # Yahoo Finance ticker symbol for the stock (e.g., "AAPL", "GOOGL", "MSFT")
YAHOO_TIMEFRAME = "5m"  # Default timeframe for Yahoo Finance downloads