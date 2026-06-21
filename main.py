from get_binance_data import SYMBOL, INTERVAL, get_btc_daily_data
from plot_chart import plot_all_charts

if __name__ == "__main__":
    data = get_btc_daily_data()
    data.to_csv(f"data/{SYMBOL}_{INTERVAL}.csv", index=False)

    plot_all_charts()
