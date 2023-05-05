import pytest
from daily_functions import public_holiday_pay, day_shift_pay, night_shift_pay, sat_loading_pay, sun_loading_pay
import csv
from pay_functions import pay_week

# Testing that each of the pay rate functions returns the right value
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

# Runs a check to see if the pay week function adds a new line to the csv.
test_file_name = "test_pay_history.csv"

def test_add(monkeypatch):
   original_length = 0
   with open(test_file_name) as f:
       reader = csv.reader(f)
       original_length = sum(1 for row in reader)
   monkeypatch.setattr('builtins.input', lambda _: "01-01-0101")
   pay_week(test_file_name)
   with open(test_file_name) as f:
       reader = csv.reader(f)
       new_length = sum(1 for row in reader)
   print(original_length)
   print(new_length)
   assert new_length == original_length + 1


