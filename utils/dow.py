import pandas as pd

DAYS = {0: "Lunes", 1: "Martes", 2: "Miércoles", 3: "Jueves", 4: "Viernes", 5: "Sábado", 6: "Domingo"}


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
