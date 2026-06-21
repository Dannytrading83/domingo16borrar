from get_binance_data import SYMBOL, INTERVAL, get_btc_daily_data
from plot_chart import plot_close_price

if __name__ == "__main__":
    data = get_btc_daily_data()
    data.to_csv(f"data/{SYMBOL}_{INTERVAL}.csv", index=False)

    plot_close_price()
