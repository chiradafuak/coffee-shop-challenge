from customer import Customer
from coffee import Coffee

c1 = Customer("Alice")
c2 = Customer("Bob")

latte = Coffee("Latte")
espresso = Coffee("Espresso")

c1.create_order(latte, 4.5)
c1.create_order(espresso, 3.0)
c2.create_order(latte, 5.0)

print("Coffees Alice ordered:", [c.name for c in c1.coffees()])
print("Customers who ordered Latte:", [c.name for c in latte.customers()])
print("Average price of Latte:", latte.average_price())
