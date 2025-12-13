from libraries.trends import trends
from libraries.position import up_day, down_day, inside_day, outside_day

def main():

    list = (6928, 6817, 6915, 6805, 6830, 6895, 6960, 7006, 6785, 6739, 6674)
    # list = scraper()  # Placeholder for future implementation
    message, type = find_trend_and_strategy(list[0], list[1], list[2], list[3], list[4], list[5], list[6], list[7], list[8], list[9], list[10])
    rsi_status, stochastic_status, adx_status = indicators()
    final_message, strat = final_strategy(type, (rsi_status, stochastic_status, adx_status))
    if type == 1:
        if strat in [1, 2, 3]:
            print(final_message + f". {message}")
        else:
            print("Review market conditions for volatility")
    elif type == 2:
        if strat in [1, 2, 3]:
            print(final_message + f". {message}")
        else:
            print("Review market conditions for volatility")
    elif type == 3:
        print(final_message + f". {message}")
    else:
        print("Review market conditions for volatility")

# Placeholder for future web scraping implementation or API integration
def scraper():
    ...

# Determine trend and suggest trading strategy
def find_trend_and_strategy(yesterday_high, yesterday_low, today_high, today_low, last_price, resistance1, resistance2, resistance3, support1, support2, support3):
    message, type = trends(yesterday_high, yesterday_low, today_high, today_low)
    if type == 1:
        return up_day(last_price, today_high, resistance1, resistance2, resistance3)
    elif type == 2:
        return down_day(last_price, today_low, support1, support2, support3)
    elif type == 3:
        return inside_day(last_price)
    elif type == 4:
        return outside_day(last_price)
    else:
        return "No clear trend detected", 0

# Analyze technical       
def indicators():
    while True:
        try:
            rsi = float(input("Enter RSI value: "))
        except ValueError:
            print("Please enter a numeric value for RSI. (e.g., 45.5)")
        else:
            if 0 <= rsi <= 100:
                break
            else:
                print("Please enter a valid RSI value between 0 and 100. (e.g., 45.5)")
    
    if rsi <= 30:
        rsi_status = "oversold"
    elif rsi >= 70:
        rsi_status = "overbought"   
    else:
        rsi_status = "neutral"

    while True:
        try:
            stochastic = float(input("Enter Stochastic value: "))
        except ValueError:
            print("Please enter a numeric value for Stochastic. (e.g., 45.5)")
        else:
            if 0 <= stochastic <= 100:
                break
            else:
                print("Please enter a valid Stochastic value between 0 and 100. (e.g., 45.5)")

    if stochastic <= 20:
        stochastic_status = "oversold"
    elif stochastic >= 80:
        stochastic_status = "overbought"
    else:
        stochastic_status = "neutral"

    while True:
        try:
            adx = float(input("Enter ADX value: "))
        except ValueError:
            print("Please enter a numeric value for ADX. (e.g., 45.5)")
        else:
            if 0 <= adx <= 100:
                break
            else:
                print("Please enter a valid ADX value between 0 and 100. (e.g., 45.5)")

    if adx < 20:
        adx_status = "weak trend"
    elif 20 <= adx <= 40:
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