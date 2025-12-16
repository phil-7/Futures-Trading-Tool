def up_day(last_price, today_high, resistance1, resistance2, resistance3):
    if last_price < resistance1:
        return f"Consider setting a buy limit order at {today_high + 3} with a stop loss at {today_high} and a target at {resistance1}", 1
    elif resistance1 <= last_price < resistance2:
        return f"Consider setting a buy limit order at {today_high + 3} with a stop loss at {today_high} and a target at {resistance2}", 1
    elif resistance2 <= last_price < resistance3:
        return f"Consider setting a buy limit order at {today_high + 3} with a stop loss at {today_high} and a target at {resistance3}", 1
    else:
        return "Review market conditions" , 0 

def down_day(last_price, today_low, support1, support2, support3):
    if last_price > support1:
        return f"Consider setting a sell limit order at {today_low - 3} with a stop loss at {today_low} and a target at {support1}", 2
    elif support2 < last_price <= support1:
        return f"Consider setting a sell limit order at {today_low - 3} with a stop loss at {today_low} and a target at {support2}", 2
    elif support3 < last_price <= support2:
        return f"Consider setting a sell limit order at {today_low - 3} with a stop loss at {today_low} and a target at {support3}", 2
    else:
        return "Review market conditions", 0

def inside_day(last_price, today_high, today_low, support1, resistance1):
    return f"Consider swing trading within 3 points of the last price for a short term strategy: Buy near {last_price - 3}, Sell near {last_price + 3}. \nFor a long term strategy, 'squeeze' the index: Set Buy limit at {today_high + 3}, stop loss at {today_high}, and buy stop at {resistance1}. Also set Sell limit at {today_low - 3}, stop loss at {today_low}, and sell stop at {support1}.", 3

def outside_day(last_price):
    return "Review market conditions", 0
