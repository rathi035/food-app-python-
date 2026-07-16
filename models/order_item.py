class OrderItem:
    
    def __init__(self, order_item_id, order_id, food_id, quantity, subtotal):

        self.order_item_id = order_item_id
        self.order_id = order_id
        self.food_id = food_id
        self.quantity = quantity
        self.subtotal = subtotal

    def display_order_item(self):

        print("Order Item ID :", self.order_item_id)
        print("Order ID :", self.order_id)
        print("Food ID :", self.food_id)
        print("Quantity :", self.quantity)
        print("Subtotal :", self.subtotal)