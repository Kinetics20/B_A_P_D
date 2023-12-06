class Price:
    eur_to_pln = 4.5
    usd_to_pln = 3.8

    def __init__(self, amount):
        if not isinstance(amount, (int, float)):
            raise ValueError('Amount must be a number (int or float')

        self.value = float(amount)
        self.value = round(self.value, 2)

    @classmethod
    def count_pln_from_usd(cls, amount):
        if not isinstance(amount, (int, float)):
            raise ValueError('Amount must be a number (int or float')

        pln_amount = amount * cls.usd_to_pln
        return cls(pln_amount)

    @classmethod
    def count_pln_from_eur(cls, amount):
        pln_amount = amount * cls.eur_to_pln
        return cls(pln_amount)

    def __str__(self):
        return f'{self.value} PLN'

    def describe(self):
        return str(self)


some_price = Price.count_pln_from_usd(200)
print(some_price)
some_other_price = Price.count_pln_from_eur(95)
print(some_other_price)
# some_price_2 = Price.count_pln_from_usd('200')
# print(some_price_2)
some_price_3 = Price(200)
print(some_price_3)

