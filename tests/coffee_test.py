import pytest
from coffee import Coffee
from customer import Customer
from order import Order

def test_coffee_initialization():
    coffee = Coffee("Espresso")
    assert coffee.name == "Espresso"

def test_coffee_name_validation():
    with pytest.raises(ValueError):
        Coffee("Es")

def test_coffee_orders():
    coffee = Coffee("Espresso")
    customer = Customer("Alice")
    order = Order(customer, coffee, 3.5)
    assert len(coffee.orders()) == 0
    coffee._orders.append(order)
    assert len(coffee.orders()) == 1
    assert coffee.orders()[0] == order

def test_coffee_customers():
    coffee = Coffee("Espresso")
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")
    order1 = Order(customer1, coffee, 3.5)
    order2 = Order(customer2, coffee, 4.0)
    coffee._orders.extend([order1, order2])
    assert len(coffee.customers()) == 2
    assert customer1 in coffee.customers()
    assert customer2 in coffee.customers()

def test_coffee_num_orders():
    coffee = Coffee("Espresso")
    customer = Customer("Alice")
    order = Order(customer, coffee, 3.5)
    coffee._orders.append(order)
    assert coffee.num_orders() == 1

def test_coffee_average_price():
    coffee = Coffee("Espresso")
    customer = Customer("Alice")
    order1 = Order(customer, coffee, 3.5)
    order2 = Order(customer, coffee, 4.5)
    coffee._orders.extend([order1, order2])
    assert coffee.average_price() == 4.0