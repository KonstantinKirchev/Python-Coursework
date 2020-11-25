import decimal

class Product:
    def __init__(self, id: int, name: str, description: str, price: decimal, quantity: int, categoryId: int):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.categoryId = categoryId
