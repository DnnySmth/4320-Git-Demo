import pytest
from datetime import date

def test_symbol():
    # Test that symbol is capitalized
    symbol = "aapl"
    assert symbol.upper() == "AAPL"
    
    # Test that symbol is between 1-7 alpha characters
    symbol = "abcdefghijklmnopqrstuvwxyz"
    with pytest.raises(AssertionError):
        assert len(symbol) > 7
    with pytest.raises(AssertionError):
        assert not symbol.isalpha()

def test_chart_type():
    # Test that chart type is 1 or 2
    chart_type = "3"
    with pytest.raises(AssertionError):
        assert chart_type in ["1", "2"]

def test_time_series():
    # Test that time series is between 1-4
    time_series = "5"
    with pytest.raises(AssertionError):
        assert time_series in ["1", "2", "3", "4"]

def test_start_date():
    # Test that start date is of the format YYYY-MM-DD
    start_date = "2021/01/01"
    with pytest.raises(ValueError):
        assert date.fromisoformat(start_date)

def test_end_date():
    # Test that end date is of the format YYYY-MM-DD
    end_date = "2022-13-01"
    with pytest.raises(ValueError):
        assert date.fromisoformat(end_date)
