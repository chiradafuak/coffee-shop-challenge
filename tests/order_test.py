import pytest
from order import Order
from customer import Customer
from coffee import Coffee

def test_order_initialization():
    customer = Customer("Alice")
    coffee = Coffee("Espresso")
    order = Order(customer, coffee, 3.5)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 3.5

def test_order_price_validation():
    customer = Customer("Alice")
    coffee = Coffee("Espresso")
    with pytest.raises(ValueError):
        Order(customer, coffee, 0.5)
    with pytest.raises(ValueError):
        Order(customer, coffee, 10.5)

def test_order_customer_validation():
    coffee = Coffee("Espresso")
    with pytest.raises(TypeError):
        Order("Alice", coffee, 3.5)

def test_order_coffee_validation():
    customer = Customer("Alice")
    with pytest.raises(TypeError):
        Order(customer, "Espresso", 3.5)