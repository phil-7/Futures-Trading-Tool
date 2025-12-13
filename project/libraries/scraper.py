import yfinance as yf
import pandas as pd

# Note: Use "ES=F" for E-mini S&P 500 futures data
# Note: Use closing prices to determine resstistance and support levels (look up equations)

emini = yf.Ticker("ES=F")
data = emini.history(period="14d", interval="1d")
# print(data)

today = data.iloc[-1]
print(today['Open'])