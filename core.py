from datetime import date
import calendar

def pick_today():
    return date.today().day

def actual_month():
    return date.today().month

def days_left(last_day):
    return last_day - pick_today()


def last_day():
    weekday, last_day = calendar.monthrange(date.today().year, actual_month())
    return last_day

def get_money():
    amount = float(input("Quantidade de dinheiro: \n"))
    return amount

def calculate_budget(money_amount, present_day, days_left):
    sugested_budget = f"R$ {(money_amount / days_left):.2f}"
    return sugested_budget

print(calculate_budget(get_money(), pick_today(), days_left(last_day())))

print(f"Dias para terminar o mês: {days_left(last_day())}")


