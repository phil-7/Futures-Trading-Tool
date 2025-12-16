from project import check_ticker, show_today_prices, show_yesterday_prices

import pytest

def test_check_ticker():
    assert check_ticker("ES=F") == True
    assert check_ticker("MOO") == True
    assert check_ticker("") == False
    assert check_ticker("1234") == False


def test_show_today_prices():
    assert show_today_prices(60, 50, 55) == "Today's Prices - High: 60, Low: 50, Close: 55"


def test_show_yesterday_prices():
    assert show_yesterday_prices(1013, 982, 997.25) == "Yesterday's Prices - High: 1013, Low: 982, Close: 997.25"
