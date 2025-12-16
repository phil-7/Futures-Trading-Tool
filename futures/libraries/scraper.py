import yfinance as yf
import pandas as pd


def scraper(ticker):

    # Fetch historical data for the given ticker
    prices = yf.Ticker(ticker)
    data = prices.history(period="60d", interval="1d")

    # Save closing prices in a list of dictionaries to make it easier to retrieve data
    closing_prices = []
    # iterrows() returns two values for each row. "Saving" first row to date to access prices in second row
    for date, row in data.iterrows():
        closing_prices.append({"high": row['High'], "low": row['Low'], "close": row['Close']})


    # Calculate resistance and support levels
    pivot_point = (closing_prices[-2]['high'] + closing_prices[-2]['low'] + closing_prices[-2]['close']) / 3

    resistance1 = (2 * pivot_point) - closing_prices[-2]['low']
    resistance2 = pivot_point + (closing_prices[-2]['high'] - closing_prices[-2]['low'])
    resistance3 = closing_prices[-2]['high'] + 2 * (pivot_point - closing_prices[-2]['low'])  

    support1 = (2 * pivot_point) - closing_prices[-2]['high']
    support2 = pivot_point - (closing_prices[-2]['high'] - closing_prices[-2]['low'])
    support3 = closing_prices[-2]['low'] - 2 * (closing_prices[-2]['high'] - pivot_point)

    return closing_prices, resistance1, resistance2, resistance3, support1, support2, support3