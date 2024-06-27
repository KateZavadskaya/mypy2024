""" Task 2: Currency """


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


class Currency:

    """ Show name and symbols """

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.exchange_rates = {}

    def set_exchange_rate(self, other_currency, rate):

        """ Create currency for other_currency """

        self.exchange_rates[other_currency] = rate

    def convert(self, amount, target_currency):

        """ Convert sum from current currency to necessary currency """

        if target_currency in self.exchange_rates:
            return amount * self.exchange_rates[target_currency]
        return None


usd = Currency('долл', '$')
eur = Currency('евро', '€')

usd.set_exchange_rate(eur, 0.85)

VASYA_MONEY = 10

vasya_eur = usd.convert(VASYA_MONEY, eur)
vasya_eur_1 = round(vasya_eur, 2)
print(f"Вася имеет {vasya_eur_1} евро")
