from datetime import date
import calendar


class TimeMachine:
    def __init__(self):
        pass

    # def __repr__(self):
    #     return f"Hoje é dia {self.get_today()}/{self.get_this_month()}"

    def get_today(self):
        return date.today().day

    def get_this_month(self):
        return date.today().month

    def get_last_monthday(self):
        return calendar.monthrange(self.get_today(), self.get_this_month())[1]


class Calculator(TimeMachine):
    def __init__(self, money_amount):
        self.money_amount = money_amount

    def __repr__(self):
        return f"Dinheiro atual: R$ {self.money_amount}"

    def add_money(self, money_amount):
        self.old_amount = self.money_amount
        self.money_amount += money_amount
        print(f"Quantia atualizada de R$ {self.old_amount} para R$ {self.money_amount}")

    def update_amount(self, money_amount):
        self.old_amount = self.money_amount
        self.money_amount = money_amount
        print(f"Quantia atualizada de R$ {self.old_amount} para R$ {self.money_amount}")
    



if __name__ == "__main__":
    budget = Calculator(500)
    

# class TimeMachine:
#     def __init__(self):
#         self.today = date.today().day
#         self.this_month = date.today().month

#     def get_last_monthday(self):
#         return calendar.monthrange(self.today, self.this_month)[1]

#     def get_days_left(self):
#         return self.get_last_monthday() - self.today


# class Calculator(TimeMachine):
#     def get_money(self):
#         self.money = float(input("Dinheiro (R$): \n"))

#     def calculate_budget(self):
#         return self.money / self.get_days_left()


# budget.get_money()
# budget.get_days_left()

# print(f"Faltam {budget.get_days_left()} dias para o final do mês.", end="")
# print(f" A sugestão de gasto diária é de R$ {budget.calculate_budget()}")

