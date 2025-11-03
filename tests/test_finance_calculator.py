import pytest
from finance_calculator import add_income, add_expense, calculate_balance


def test_add_income():
    assert add_income(100, 50) == 150
    assert add_income(0, 100) == 100

def test_add_income_negative():
    with pytest.raises(ValueError, match="Income cannot be negative"):
        add_income(100, -10)

def test_add_expense():
    assert add_expense(100, 30) == 70
    assert add_expense(50, 50) == 10

def test_add_expense_negative():
    with pytest.raises(ValueError, match="Expense cannot be negative"):
        add_expense(100, -10)

def test_add_expense_insufficient():
    with pytest.raises(ValueError, match="Insufficient funds"):
        add_expense(20, 50)

def test_calculate_balance():
    income = [1000, 200]
    expenses = [300, 150]
    assert calculate_balance(income, expenses) == 750