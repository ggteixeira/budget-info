from datetime import date


def pick_today():
    today = date.today().day
    return today

def actual_month():
    return date.today().month

def days_left():
    return 31 - pick_today()


print(f"Faltam {days_left()} para acabar o mês")