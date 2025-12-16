from libraries.scraper import scraper
from libraries.trends import trends
from libraries.position import up_day, down_day, inside_day, outside_day
from ta.trend import ADXIndicator

import pandas as pd

def main():
    while True:
        # Prompt user for ticker symbol
        print("Ticker(s): E-mini S&P 500 Futures (ES=F) - Moo Moo (MOO)")
        ticker = input("Enter ticker symbol: ").strip()
        status = check_ticker(ticker)
        if status:
            break


    # Unpack prices and pivot points from scraper
    prices, resistance1, resistance2, resistance3, support1, support2, support3 = scraper(ticker)


    # Unpack message and type from trend/strategy finder
    message, type = find_trend_and_strategy(prices[-2]['high'], prices[-2]['low'], prices[-1]['high'], prices[-1]['low'], prices[-1]['close'], resistance1, resistance2, resistance3, support1, support2, support3)

    # Get status of indicators
    rsi_status, stochastic_status, adx_status = indicators(prices)

    # Save today's prices and show user
    today_high = prices[-1]['high']
    today_low = prices[-1]['low']
    today_close = prices[-1]['close']
    
    stp = show_today_prices(today_high, today_low, today_close)
    print(stp)

    # Save yesterday's prices and show user
    y_high = prices[-2]['high']
    y_low = prices[-2]['low']
    y_close = prices[-2]['close']
    
    syp = show_yesterday_prices(y_high, y_low, y_close)
    print(syp)
    print("")

    # Get final strategy based on trend type and indicators
    final_message, strat = final_strategy(type, (rsi_status, stochastic_status, adx_status))
    if type == 1:
        if strat in [1, 2, 3]:
            print("Up Day Strategy:")
            print(final_message + f". {message}")
        else:
            print("Up Day Strategy:")
            print("Review market conditions for volatility")
    elif type == 2:
        if strat in [1, 2, 3]:
            print("Down Day Strategy:")
            print(final_message + f". {message}")
        else:
            print("Down Day Strategy:")
            print("Review market conditions for volatility")
    elif type == 3:
        print("Inside Day Strategy:")
        print(final_message + f". {message}")
    else:
        print("Outside Day Strategy:")
        print("Review market conditions for volatility")

# Get Ticker
def check_ticker(ticker):
    tickers_symbols = ("ES=F", "MOO")
    # This functionality could've been in scraper(), but too many ticker symbols
    while True:
        if ticker in tickers_symbols:
            return True
        else:
            print("ENTER VALID TICKER\n")
            return False
        
# Print today's prices
def show_today_prices(h, l, c):
    return f"Today's Prices - High: {h}, Low: {l}, Close: {c}"

# Print yesterday's prices
def show_yesterday_prices(h, l, c):
    return f"Yesterday's Prices - High: {h}, Low: {l}, Close: {c}"

# Determine trend and suggest trading strategy
def find_trend_and_strategy(yesterday_high, yesterday_low, today_high, today_low, last_price, resistance1, resistance2, resistance3, support1, support2, support3):
    message, type = trends(yesterday_high, yesterday_low, today_high, today_low)
    if type == 1:
        return up_day(last_price, today_high, resistance1, resistance2, resistance3)
    elif type == 2:
        return down_day(last_price, today_low, support1, support2, support3)
    elif type == 3:
        return inside_day(last_price, today_high, today_low, support1, resistance1)
    elif type == 4:
        return outside_day(last_price)
    else:
        return "No clear trend detected", 0

# Analyze technical       
def indicators(prices):
    gain, loss = 0.0, 0.0
    
    for i in range(2, len(prices)-1):
        change = float(prices[i + 1]['close']) - float(prices[i]['close'])

        if change >= 0.0:
             gain += change
        else:
            loss += abs(change)
    
    avg_gain = float(float(gain) / 14.0)  
    avg_loss = float(float(loss) / 14.0)

    if avg_loss == 0:
        rs = 0.0
    else:
        rs = float(avg_gain / avg_loss)
    
    rsi = float(100 - float((float(100) / float(1.0 + rs))))
    print(f"Relative Strength Index: {rsi:.2f}")

    # Determine RSI status
    if rsi <= 30:
        rsi_status = "oversold"
    elif rsi >= 70:
        rsi_status = "overbought"   
    else:
        rsi_status = "neutral"

    # Stochastic calculation
    high_14 = max([price['high'] for price in prices[-14:]])
    low_14 = min([price['low'] for price in prices[-14:]])  
    stochastic = ((prices[-1]['close'] - low_14 ) / (high_14 - low_14)) * 100  
    

    print(f"Stochastic: {stochastic:.2f}")

    # Determine stochastic status
    if stochastic <= 20:
        stochastic_status = "oversold"
    elif stochastic >= 80:
        stochastic_status = "overbought"
    else:
        stochastic_status = "neutral"

    # ADX calculation (simplified version)
    # ADX calculation code taken from online source
    df = pd.DataFrame(prices) 
    adx_indicator = ADXIndicator(high=df['high'], low=df['low'], close=df['close'], window=14)
    adx = adx_indicator.adx().iloc[-1]  
    

    print(f"Average Directional Index (ADX): {adx:.2f}\n")
    
    # Determine ADX status
    if adx < 25:
        adx_status = "weak trend"
    elif 25 <= adx <= 40:
        adx_status = "strengthening trend"
    else:
        adx_status = "strong trend"

    return rsi_status, stochastic_status, adx_status

# Combine trend type and indicator analysis for final strategy
def final_strategy(type, indicators):
    rsi_status, stochastic_status, adx_status = indicators
    if type == 1:  # Uptrend
        if rsi_status == "oversold" and stochastic_status == "oversold" and adx_status == "strong trend":
            return "Very strong buy signal in uptrend", 1
        elif rsi_status == "oversold" and stochastic_status == "oversold" and adx_status == "strengthening trend":
            return "Strong buy signal in uptrend", 2
        elif rsi_status == "neutral" and stochastic_status == "neutral" and adx_status in ["strengthening trend", "strong trend"]:
            return "Moderate buy signal in uptrend", 3
        else:
            return "Cautious buy signal in uptrend", 0
    elif type == 2:  # Downtrend
        if rsi_status == "overbought" and stochastic_status == "overbought" and adx_status == "strong trend":
            return "Very strong sell signal in downtrend", 1
        elif rsi_status == "overbought" and stochastic_status == "overbought" and adx_status == "strengthening trend":
            return "Strong sell signal in downtrend", 2
        elif rsi_status == "neutral" and stochastic_status == "neutral" and adx_status in ["strengthening trend", "strong trend"]:
            return "Moderate sell signal in downtrend", 3
        else:
            return "Cautious sell signal in downtrend", 0
    elif type == 3:  # Inside day
        return "Consider swing trading strategies", 1
    elif type == 4:  # Outside day
        return "Review market conditions for volatility", 0
    else:
        return "No clear strategy due to lack of trend", 0
    
if __name__ == "__main__":
    main()
