import pytest
from ..customer import Customer
from ..coffee import Coffee

def test_customer_name_constraints():
    with pytest.raises(ValueError):
        Customer("")
    with pytest.raises(ValueError):
        Customer("a" * 16)
    with pytest.raises(ValueError):
        Customer(123)

def test_create_order_and_coffees():
    c = Customer("Alice")
    coffee = Coffee("Latte")
    order = c.create_order(coffee, 5.0)
    assert order in c.orders()
    assert coffee in c.coffees()
