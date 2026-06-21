import pandas as pd

DECIMALS = 3


def round_btc_values(df, decimals=DECIMALS):
    numeric_cols = df.select_dtypes(include="float").columns
    df[numeric_cols] = df[numeric_cols].round(decimals)
    return df


if __name__ == "__main__":
    df = pd.read_csv("data/BTCUSDT_1h.csv")
    df = round_btc_values(df)
    df.to_csv("data/BTCUSDT_1h.csv", index=False)
    print(df.tail())
