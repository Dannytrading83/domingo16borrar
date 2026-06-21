import requests
import pandas as pd

from config import BINANCE_API_ENDPOINT, BINANCE_API_KEY

SYMBOL = "BTCUSDT"
INTERVAL = "1d"

COLUMNS = [
    "open_time", "open", "high", "low", "close", "volume",
    "close_time", "quote_asset_volume", "number_of_trades",
    "taker_buy_base_volume", "taker_buy_quote_volume", "ignore",
]


def get_btc_daily_data(limit=1000):
    response = requests.get(
        f"{BINANCE_API_ENDPOINT}/api/v3/klines",
        params={"symbol": SYMBOL, "interval": INTERVAL, "limit": limit},
        headers={"X-MBX-APIKEY": BINANCE_API_KEY},
    )
    response.raise_for_status()

    df = pd.DataFrame(response.json(), columns=COLUMNS)
    df["open_time"] = pd.to_datetime(df["open_time"], unit="ms")
    df["close_time"] = pd.to_datetime(df["close_time"], unit="ms")
    for col in ["open", "high", "low", "close", "volume", "quote_asset_volume",
                "taker_buy_base_volume", "taker_buy_quote_volume"]:
        df[col] = df[col].astype(float)

    return df


if __name__ == "__main__":
    data = get_btc_daily_data()
    print(data.tail())
    data.to_csv(f"{SYMBOL}_{INTERVAL}.csv", index=False)
