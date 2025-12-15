from project.project import get_ticker, show_today_prices, show_yesterday_prices

import pytest

def test_get_ticker():
    assert get_ticker("ES=F") == "ES=F"
    assert get_ticker("MOO") == "ENTER VALID TICKER"
    assert get_ticker("") == "ENTER VALID TICKER"
    assert get_ticker("1234") == "ENTER VALID TICKER"


def test_show_today_prices():
    assert show_today_prices(60, 50, 55) == "Today's Prices - High: 60, Low: 50, Close: 55"


def test_show_yesterday_prices():
    assert show_yesterday_prices(1013, 982, 997.25) == "Yesterday's Prices - High: 1013, Low: 982, Close: 997.25"