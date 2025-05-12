import pytest
from is_leap_year import is_leap_year

def test_regular_leap_year():
    assert is_leap_year(2024) is True

def test_common_year():
    assert is_leap_year(2023) is False

def test_century_not_leap():
    assert is_leap_year(1900) is False

def test_century_leap():
    assert is_leap_year(2000) is True

def test_year_zero_or_negative():
    with pytest.raises(ValueError):
        is_leap_year(0)

    with pytest.raises(ValueError):
        is_leap_year(-400)

def test_non_integer_input():
    with pytest.raises(ValueError):
        is_leap_year("2024")

    with pytest.raises(ValueError):
        is_leap_year(2024.0)