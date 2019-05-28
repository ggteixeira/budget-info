from datetime import date
import calendar

def pick_today():
    return date.today().day

def actual_month():
    return date.today().month

def days_left():
    return 31 - pick_today()


# print(f"Faltam {days_left()} para acabar o mês")

def last_day():
    weekday, last_day = calendar.monthrange(date.today().year, actual_month())
    return last_day

# print(calendar.monthrange(date.today().year, actual_month()))

print(f"Este mês tem {last_day()} dias.")