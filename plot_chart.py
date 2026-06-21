import glob
import os

import pandas as pd
import matplotlib.pyplot as plt

DATA_DIR = "data"
CHARTS_DIR = "charts"


def plot_close_price(data_path, charts_dir=CHARTS_DIR):
    df = pd.read_csv(data_path, parse_dates=["open_time"])

    name = os.path.splitext(os.path.basename(data_path))[0]
    output_path = f"{charts_dir}/{name}_close.png"

    plt.figure(figsize=(12, 6))
    plt.plot(df["open_time"], df["close"])
    plt.title(f"{name} Close Price")
    plt.xlabel("Fecha")
    plt.ylabel("Precio de cierre (USDT)")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

    return output_path


def plot_all_charts(data_dir=DATA_DIR, charts_dir=CHARTS_DIR):
    for data_path in glob.glob(f"{data_dir}/*.csv"):
        plot_close_price(data_path, charts_dir)


if __name__ == "__main__":
    plot_all_charts()
