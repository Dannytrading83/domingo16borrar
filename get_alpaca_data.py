import requests
import pandas as pd

from config import ALPACA_DATA_ENDPOINT, ALPACA_API_KEY, ALPACA_API_SECRET, TIMEFRAME

SYMBOL = "AAPL"

TIMEFRAME_MAP = {
    "1H": "1Hour", "1h": "1Hour",
    "4H": "4Hour", "4h": "4Hour",
    "1D": "1Day",  "1d": "1Day",
}
INTERVAL = TIMEFRAME_MAP.get(TIMEFRAME, "4Hour")

HEADERS = {
    "APCA-API-KEY-ID": ALPACA_API_KEY,
    "APCA-API-SECRET-KEY": ALPACA_API_SECRET,
}


def get_stock_data(symbol=SYMBOL, limit=1000, start="2020-01-01"):
    bars = []
    page_token = None

    while len(bars) < limit:
        params = {
            "timeframe": INTERVAL,
            "limit": min(1000, limit - len(bars)),
            "adjustment": "all",
            "start": start,
        }
        if page_token:
            params["page_token"] = page_token

        response = requests.get(
            f"{ALPACA_DATA_ENDPOINT}/stocks/{symbol}/bars",
            params=params,
            headers=HEADERS,
        )
        response.raise_for_status()
        data = response.json()

        page_bars = data.get("bars") or []
        bars.extend(page_bars)

        page_token = data.get("next_page_token")
        if not page_token:
            break

    df = pd.DataFrame(bars)
    if df.empty:
        return df

    df.rename(columns={
        "t": "open_time",
        "o": "open",
        "h": "high",
        "l": "low",
        "c": "close",
        "v": "volume",
        "vw": "vwap",
        "n": "number_of_trades",
    }, inplace=True)
    df["open_time"] = pd.to_datetime(df["open_time"])
    for col in ["open", "high", "low", "close", "volume", "vwap"]:
        if col in df.columns:
            df[col] = df[col].astype(float)

    return df


if __name__ == "__main__":
    data = get_stock_data()
    print(data.tail())
    data.to_csv(f"data/{SYMBOL}_{TIMEFRAME}.csv", index=False)
