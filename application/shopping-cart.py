import decimal
from datetime import datetime
from order_status import OrderStatus

class ShoppingCart:
    def __init__(self, id: int, status: OrderStatus, totalPrice: decimal, dateOfOrder: datetime, dateOfDelivery: datetime, userId: int):
        self.id = id
        self.status = status
        self.totalPrice = totalPrice
        self.dateOfOrder = dateOfOrder
        self.dateOfDelivery = dateOfDelivery
        self.userId = userId