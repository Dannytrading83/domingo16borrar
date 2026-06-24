"""
Carga el CSV de EUR/USD 1 minuto en un DataFrame y lo guarda en data/.

- Lee el CSV original descargado (timeframe 1 minuto, precio BID).
- El DataFrame resultante se llama euusd_1M.
- Se guarda una copia normalizada en data/euusd_1M.csv.
"""

from pathlib import Path

import pandas as pd

from utils.dow import get_dow

# --- Rutas ---
DATA_DIR = Path(__file__).resolve().parent / "data"
SOURCE = DATA_DIR / "EUR-USD_1Minute_BID_2026-06-17_00_00-23_59_Etc_UTC.csv"
OUTPUT = DATA_DIR / "euusd_1M.csv"

# --- Carga ---
# La primera columna ("Etc/UTC") es el timestamp en UTC -> lo usamos como índice.
euusd_1M = pd.read_csv(SOURCE, parse_dates=["Etc/UTC"])
euusd_1M = euusd_1M.rename(columns={"Etc/UTC": "timestamp"})
euusd_1M = euusd_1M.set_index("timestamp")

# --- DOW ---
euusd_1M["dow"] = euusd_1M.index.map(lambda ts: get_dow(ts)[0])
euusd_1M["dow_name"] = euusd_1M.index.map(lambda ts: get_dow(ts)[1])

# --- Guardar ---
euusd_1M.to_csv(OUTPUT)

print(euusd_1M)
