import pytest
from ..coffee import Coffee
from ..customer import Customer

def test_coffee_name_validation():
    with pytest.raises(ValueError):
        Coffee("A")
    assert Coffee("Latte").name == "Latte"

def test_num_orders_and_avg_price():
    coffee = Coffee("Espresso")
    c = Customer("Bob")
    c.create_order(coffee, 4.0)
    c.create_order(coffee, 6.0)
    assert coffee.num_orders() == 2
    assert coffee.average_price() == 5.0
