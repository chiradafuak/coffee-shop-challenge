import pytest
from ..order import Order
from ..customer import Customer
from ..coffee import Coffee

def test_order_constraints():
    c = Customer("Test")
    coffee = Coffee("Latte")

    with pytest.raises(ValueError):
        Order(c, coffee, 0.5)
    with pytest.raises(TypeError):
        Order("not-a-customer", coffee, 2.0)
    with pytest.raises(TypeError):
        Order(c, "not-a-coffee", 2.0)

    order = Order(c, coffee, 3.5)
    assert order.price == 3.5
    assert order.customer == c
    assert order.coffee == coffee
