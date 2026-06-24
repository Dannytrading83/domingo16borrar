import glob
import os

import pandas as pd
import matplotlib.pyplot as plt

DATA_DIR = "data"
CHARTS_DIR = "charts"


TIME_COLS = ["open_time", "timestamp", "Etc/UTC", "datetime"]


def plot_close_price(data_path, charts_dir=CHARTS_DIR):
    df = pd.read_csv(data_path)

    time_col = next((c for c in df.columns if c in TIME_COLS), df.columns[0])
    df[time_col] = pd.to_datetime(df[time_col], utc=True)

    name = os.path.splitext(os.path.basename(data_path))[0]
    output_path = f"{charts_dir}/{name}_close.png"

    close_col = "close" if "close" in df.columns else "Close"

    plt.figure(figsize=(12, 6))
    plt.plot(df[time_col], df[close_col])
    plt.title(f"{name} Close Price")
    plt.xlabel("Fecha")
    plt.ylabel("Precio de cierre (USD)")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

    return output_path


def plot_all_charts(data_dir=DATA_DIR, charts_dir=CHARTS_DIR):
    for data_path in glob.glob(f"{data_dir}/*.csv"):
        plot_close_price(data_path, charts_dir)


if __name__ == "__main__":
    plot_all_charts()
