from datetime import date
import calendar

def last_day():
    weekday, last_day = calendar.monthrange(date.today().year, date.today().month)
    return weekday

print(last_day())

