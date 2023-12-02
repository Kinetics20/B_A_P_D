class Cart:
    def __init__(self):
        self.products = []

    def add(self, price, name):
        self.products.append(
            (price, name,)
        )

    def summary(self):
        return self.products


class Discount20PercentCart(Cart):
    def summary(self):
        # return [(price * 0.8, name) for price, name in self.products]

        after_discount = []
        for price, name in self.products:
            after_discount.append(
                (price * 0.8, name,)
            )
        return after_discount


class Above3ProductsCheapestFreeCart(Cart):
    def summary(self):
        if len(self.products) <= 3:
            return self.products

        products_copy = sorted(self.products)
        cheapest_product = products_copy[0]  # 0 = początek listy = najtańszy
        cheapest_product_name = cheapest_product[1]  # 0: cena, 1: nazwa
        products_copy[0] = (0, cheapest_product_name)
        return products_copy
