import yfinance as yf
import pandas as pd

# Note: Use "ES=F" for E-mini S&P 500 futures data
# Note: Use closing prices to determine resstistance and support levels (look up equations)
def scraper(ticker):

    prices = yf.Ticker(ticker)
    data = prices.history(period="14d", interval="1d")

    today = data.iloc[-1]
    latest_close = int(today['Close'])
    today_high = int(today['High'])
    today_low = int(today['Low'])

    yesterday = data.iloc[-2]
    yesterday_high = int(yesterday['High'])
    yesterday_low = int(yesterday['Low'])
    yesterday_close = int(yesterday['Close'])
    

    # Calculate resistance and support levels
    pivot_point = (yesterday_high + yesterday_low + yesterday_close) / 3

    resistance1 = (2 * pivot_point) - yesterday_low
    resistance2 = pivot_point + (yesterday_high - yesterday_low)
    resistance3 = yesterday_high + 2 * (pivot_point - yesterday_low)    

    support1 = (2 * pivot_point) - yesterday_high
    support2 = pivot_point - (yesterday_high - yesterday_low)
    support3 = yesterday_low - 2 * (yesterday_high - pivot_point)

    return yesterday_high, yesterday_low, today_high, today_low, latest_close, resistance1, resistance2, resistance3, support1, support2, support3