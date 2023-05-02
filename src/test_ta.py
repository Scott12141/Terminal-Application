import pytest
from daily_functions import public_holiday_pay, day_shift_pay, night_shift_pay, sat_loading_pay, sun_loading_pay

def test_basic():
    assert "hello world" == "hello world"

def test_ph_pay():
    assert public_holiday_pay(50, 10) == 1250

def test_ds_pay():
    assert day_shift_pay(50, 10) == 500

def test_ns_pay():
    assert night_shift_pay(50, 10) == 625

def test_sat_pay():
    assert sat_loading_pay(50, 10) == 750

def test_sun_pay():
    assert sun_loading_pay(50, 10) == 900