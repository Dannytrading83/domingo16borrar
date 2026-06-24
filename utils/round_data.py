import pandas as pd

DECIMALS = 3


def round_numeric_values(df, decimals=DECIMALS):
    numeric_cols = df.select_dtypes(include="float").columns
    df[numeric_cols] = df[numeric_cols].round(decimals)
    return df


if __name__ == "__main__":
    df = pd.read_csv("data/AAPL_4H.csv")
    df = round_numeric_values(df)
    df.to_csv("data/AAPL_4H.csv", index=False)
    print(df.tail())
