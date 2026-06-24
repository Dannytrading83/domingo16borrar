import pandas as pd

SOURCE = "data/EUR-USD_1Minute_BID_2026-06-17_00_00-23_59_Etc_UTC.csv"
OUTPUT = "data/EURUSD_1m.csv"

EURUSD_1m = pd.read_csv(SOURCE, parse_dates=["Etc/UTC"])
EURUSD_1m.rename(columns={"Etc/UTC": "datetime"}, inplace=True)
EURUSD_1m.columns = [c.lower() for c in EURUSD_1m.columns]

EURUSD_1m.to_csv(OUTPUT, index=False)

print(EURUSD_1m.to_string())
