# Aquí pongo las variables del sistema
import os
from dotenv import load_dotenv

load_dotenv()

TIMEFRAME = "4H"  #Timeframe for data analysis (e.g., "1h", "4h", "1d")

VALOR_EMA_RAPIDA = 12
VALOR_EMA_LENTA = 26

# Binance
BINANCE_API_ENDPOINT = "https://api.binance.com"
BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET")