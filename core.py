from datetime import date
import calendar


class TimeMachine:
    def __init__(self):
        self.today = date.today().day
        self.this_month = date.today().month

    def get_last_monthday(self):
        return calendar.monthrange(self.today, self.this_month)[1]

    def get_days_left(self):
        days_left = self.get_last_monthday() - self.today
        return days_left


class Calculator(timeMachine):
    def get_money(self):
        self.money = float(input("Dinheiro (R$): \n"))

    def calculate_budget(self):
        budget = self.money / self.get_days_left()
        return budget


if __name__ == "__main__":
    budget = Calculator()

    budget.get_money()
    budget.get_days_left()

    print(budget.calculate_budget())

