class Payment:
    
    def __init__(self, payment_id, order_id, amount, payment_method, payment_status):

        self.payment_id = payment_id
        self.order_id = order_id
        self.amount = amount
        self.payment_method = payment_method
        self.payment_status = payment_status

    def display_payment(self):

        print("Payment ID :", self.payment_id)
        print("Order ID :", self.order_id)
        print("Amount :", self.amount)
        print("Payment Method :", self.payment_method)
        print("Payment Status :", self.payment_status)