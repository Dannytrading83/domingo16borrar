import pandas as pd

DAYS = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}


def add_dow(df, time_col="open_time"):
    df["dow"] = pd.to_datetime(df[time_col]).dt.dayofweek
    df["dow_name"] = df["dow"].map(DAYS)
    return df


def get_dow(dt):
    dt = pd.to_datetime(dt)
    return dt.dayofweek, DAYS[dt.dayofweek]


if __name__ == "__main__":
    from datetime import datetime
    idx, name = get_dow(datetime.now())
    print(f"Today: {name} (dow={idx})")
