import pandas as pd


def add_max_dia(df, col="High"):
    fecha = df.index.normalize()
    max_por_dia = df.groupby(fecha)[col].transform("max")
    df["is_max_dia"] = df[col] == max_por_dia
    return df
