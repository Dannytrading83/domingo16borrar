from pathlib import Path

import pandas as pd
import yfinance as yf

from config import LISTA_TICKERS, YAHOO_TIMEFRAME

PERIOD_MAP = {
    "1m": "7d", "2m": "60d", "5m": "60d", "15m": "60d",
    "30m": "60d", "60m": "60d", "1h": "60d", "1d": "2y",
}
PERIOD = PERIOD_MAP.get(YAHOO_TIMEFRAME, "60d")

DATA_DIR = Path(__file__).resolve().parent / "data"


def get_yahoo_data(ticker, interval=YAHOO_TIMEFRAME, period=PERIOD):
    df = yf.download(ticker, interval=interval, period=period, auto_adjust=True, progress=False)
    df.columns = df.columns.get_level_values(0)
    df.index.name = "open_time"
    df.columns = [c.lower() for c in df.columns]
    return df


def append_yahoo_data(ticker, output):
    new_df = get_yahoo_data(ticker)

    if output.exists():
        existing = pd.read_csv(output, index_col="open_time", parse_dates=True)
        combined = pd.concat([existing, new_df])
        combined = combined[~combined.index.duplicated(keep="last")]
        combined.sort_index(inplace=True)
        nuevas = len(combined) - len(existing)
    else:
        combined = new_df
        nuevas = len(combined)

    combined.to_csv(output)
    return len(combined), nuevas


if __name__ == "__main__":
    for ticker in LISTA_TICKERS:
        output = DATA_DIR / f"{ticker}_{YAHOO_TIMEFRAME}.csv"
        total, nuevas = append_yahoo_data(ticker, output)
        print(f"{ticker}: {nuevas} filas nuevas añadidas | total: {total} -> {output.name}")
