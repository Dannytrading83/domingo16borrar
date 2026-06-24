from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
SOURCE = DATA_DIR / "euusd_1M.csv"


def find_max_min(df):
    max_idx = df["High"].idxmax()
    min_idx = df["Low"].idxmin()

    max_row = df.loc[max_idx]
    min_row = df.loc[min_idx]

    print(f"MAXIMO DEL DIA -> High: {max_row['High']}  |  timestamp: {max_idx}  |  hora NY: {max_row['hora_ny']}")
    print(f"MINIMO DEL DIA -> Low:  {min_row['Low']}  |  timestamp: {min_idx}  |  hora NY: {min_row['hora_ny']}")

    return max_row, min_row


if __name__ == "__main__":
    df = pd.read_csv(SOURCE, encoding="utf-8", index_col="timestamp")
    find_max_min(df)
