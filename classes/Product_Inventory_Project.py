class Product:
    def __init__(self, product_id, price, quantity):
        self.product_id = product_id
        self.price = price
        self.quantity = quantity

    def calculate_value(self):
        return self.price * self.quantity


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_inventory_value(self):
        total_value = 0
        for product in self.products:
            total_value += product.calculate_value()
        return total_value


# Example usage:
if __name__ == "__main__":

    product1 = Product(1, 10, 5)
    product2 = Product(2, 20, 3)
    product3 = Product(3, 5, 10)

    inventory = Inventory()
    inventory.add_product(product1)
    inventory.add_product(product2)
    inventory.add_product(product3)

    total_value = inventory.calculate_inventory_value()
    print(f"Total inventory value: ${total_value}")
