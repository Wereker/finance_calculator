def add_income(balance, income):
    """Добавить доход к балансу."""
    if income < 0:
        raise ValueError("Income cannot be negative")
    return balance + income

def add_expense(balance, expense):
    """Вычесть расход из баланса."""
    if expense < 0:
        raise ValueError("Expense cannot be negative")
    if balance < expense:
        raise ValueError("Insufficient funds")
    return balance - expense

def calculate_balance(income_list, expense_list):
    """Рассчитать итоговый баланс по спискам доходов и расходов."""
    balance = 0
    for inc in income_list:
        balance = add_income(balance, inc)
    for exp in expense_list:
        balance = add_expense(balance, exp)
    return balance


if __name__ == "__main__":
    inc = [2000, 600]
    exp = [300, 200, 100]
    print("Final balance:", calculate_balance(inc, exp))