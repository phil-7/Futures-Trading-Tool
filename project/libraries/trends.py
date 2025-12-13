def trends(yesterday_high, yesterday_low, today_high, today_low):
    if today_high > yesterday_high and today_low > yesterday_low:
        return "uptrend", 1
    elif today_high < yesterday_high and today_low < yesterday_low:
        return "downtrend", 2
    elif today_high < yesterday_high and today_low > yesterday_low:
        return "inside day", 3
    elif today_high > yesterday_high and today_low < yesterday_low:
        return "outside day", 4
    else:
        return "no clear trend", 5