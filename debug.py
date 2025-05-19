import sys
from customer import Customer
from coffee import Coffee
from order import Order

def main():
    # Example usage
    customer = Customer("Alice")
    coffee = Coffee("Espresso")
    order = Order(customer, coffee, 3.5)

    print(f"Customer: {customer.name}")
    print(f"Coffee: {coffee.name}")
    print(f"Order Price: {order.price}")

if __name__ == "__main__":
    main()