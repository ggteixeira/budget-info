from datetime import date
import calendar


class TimeMachine:
    def __init__(self):
        self.today = date.today().day
        self.this_month = date.today().month

    def get_last_monthday(self):
        return calendar.monthrange(self.today, self.this_month)[1]

    def get_days_left(self):
        return self.get_last_monthday() - self.today


class Calculator(TimeMachine):
    def get_money(self):
        self.money = float(input("Dinheiro (R$): \n"))

    def calculate_budget(self):
        return self.money / self.get_days_left()


if __name__ == "__main__":
    budget = Calculator()

    budget.get_money()
    budget.get_days_left()

    print(f"Faltam {budget.get_days_left()} dias para o final do mês.", end="")
    print(f" A sugestão de gasto diária é de R$ {budget.calculate_budget()}")

