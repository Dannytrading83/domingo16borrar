from pathlib import Path

import yfinance as yf

from config import TICKER_YAHOO, TIMEFRAME

# yfinance no soporta 4H nativo -> se mapea al intervalo más cercano disponible
TIMEFRAME_MAP = {
    "1H": "1h",
    "4H": "1h",
    "1D": "1d",
}
INTERVAL = TIMEFRAME_MAP.get(TIMEFRAME, "1d")
PERIOD = "60d" if INTERVAL == "1h" else "2y"

DATA_DIR = Path(__file__).resolve().parent / "data"
OUTPUT = DATA_DIR / f"{TICKER_YAHOO}_{TIMEFRAME}.csv"


def get_yahoo_data(ticker=TICKER_YAHOO, interval=INTERVAL, period=PERIOD):
    df = yf.download(ticker, interval=interval, period=period, auto_adjust=True, progress=False)
    df.columns = df.columns.get_level_values(0)
    df.index.name = "open_time"
    df.columns = [c.lower() for c in df.columns]
    return df


if __name__ == "__main__":
    data = get_yahoo_data()
    data.to_csv(OUTPUT)
    print(data)
    print(f"\nGuardado en: {OUTPUT}")
