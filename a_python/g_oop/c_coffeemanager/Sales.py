from Order import Order
from Payment import Payment
class Sales:
    
    def take_order(self, order: Order):
        order.execute()
        payment = Payment(order)
        payment.execute()
        return payment