""" Task 2: bank deposit """


class Bank:

    """ h """
    persent = 30

    def __init__(self, summ_dep, dep_time, dep_n):
        self.summ_dep = summ_dep
        self.dep_time = dep_time * 12
        self.dep_n = dep_n

    def dep(self, persent):

        """ j """
        self.persent = persent
        monthly_persent = persent/100/12
        persent_total = self.summ_dep * (1 + monthly_persent) ** self.dep_time
        return persent_total

    def x1(self):

        """ for pylint :(, no need in code """

    def x2(self):

        """  for pylint :(, no need in code """


money_account_1 = Bank(100, 5, "1")

total_amount_over_time = money_account_1.dep(30)

print(f"Over {money_account_1.dep_time} mounth:")
print(f"acount '{money_account_1.dep_n}' will be {total_amount_over_time}")
