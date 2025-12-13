from libraries.trends import trends
from libraries.position import up_day, down_day, inside_day, outside_day

def main():

    list = (6928, 6817, 6915, 6805, 6830, 6895, 6960, 7006, 6785, 6739, 6674)
    # list = scraper()  # Placeholder for future implementation
    message = find_trend_and_strategy(list[0], list[1], list[2], list[3], list[4], list[5], list[6], list[7], list[8], list[9], list[10])
    print(message)

def scraper():
    ...


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
        return "No clear trend detected"


def function_n():
    ...


if __name__ == "__main__":
    main()