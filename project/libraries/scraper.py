import yfinance as yf

# Note: Use "ES=F" for E-mini S&P 500 futures data
# Note: Use closing prices to determine resstistance and support levels (look up equations)

emini = yf.Ticker("ES=F")
data = emini.history(period="5d", interval="1d")
print(data)
