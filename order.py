class Order:
    def __init__(self, customer, coffee, price):
        self._customer = None
        self._coffee = None
        self._price = None
        self.customer = customer
        self.coffee = coffee
        self.price = price

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        if isinstance(value, Customer):
            self._customer = value
        else:
            raise TypeError("Customer must be an instance of Customer.")

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        if isinstance(value, Coffee):
            self._coffee = value
        else:
            raise TypeError("Coffee must be an instance of Coffee.")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if isinstance(value, (float, int)) and 1.0 <= value <= 10.0:
            self._price = float(value)
        else:
            raise ValueError("Price must be a float between 1.0 and 10.0.")