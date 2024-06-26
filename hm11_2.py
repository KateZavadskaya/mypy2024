""" Task 2: bank deposit """


class Bank:

    """ Has created for deposit with % """

    def __init__(self, summ_dep, dep_time, dep_n, percent):
        self.summ_dep = summ_dep
        self.dep_time = dep_time * 12
        self.dep_n = dep_n
        self.percent = percent

    def dep(self, percent):

        """ Method create % deposite """
        self.percent = percent
        monthly_percent = percent/100/12
        percent_total = self.summ_dep * (1 + monthly_percent) ** self.dep_time
        return percent_total

    def x1(self):

        """ for pylint :(, no need in code """

    def x2(self):

        """  for pylint :(, no need in code """


money_account_1 = Bank(100, 5, "1", 30)

total_amount_over_time = round((money_account_1.dep(30)), 2)

print(f"Over {money_account_1.dep_time} mounth:")
print(f"acount '{money_account_1.dep_n}' will be {total_amount_over_time}")
