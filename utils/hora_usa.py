from zoneinfo import ZoneInfo

NY_TZ = ZoneInfo("America/New_York")


def add_hora_ny(df):
    ny_times = df.index.tz_convert(NY_TZ)
    df["hora_ny"] = ny_times.strftime("%H:%M")
    return df
