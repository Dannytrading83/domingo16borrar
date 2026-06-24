from get_alpaca_data import SYMBOL, TIMEFRAME, get_stock_data
from plot_chart import plot_all_charts

if __name__ == "__main__":
    data = get_stock_data()
    data.to_csv(f"data/{SYMBOL}_{TIMEFRAME}.csv", index=False)

    plot_all_charts()
