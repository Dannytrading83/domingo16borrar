import pandas as pd
import matplotlib.pyplot as plt

DATA_PATH = "data/BTCUSDT_1h.csv"
OUTPUT_PATH = "charts/BTCUSDT_close.png"


def plot_close_price(data_path=DATA_PATH, output_path=OUTPUT_PATH):
    df = pd.read_csv(data_path, parse_dates=["open_time"])

    plt.figure(figsize=(12, 6))
    plt.plot(df["open_time"], df["close"])
    plt.title("BTCUSDT Close Price")
    plt.xlabel("Fecha")
    plt.ylabel("Precio de cierre (USDT)")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


if __name__ == "__main__":
    plot_close_price()
