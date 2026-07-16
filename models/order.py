class Order:
    
    def __init__(self, order_id, customer_id, restaurant_id, order_date, total_amount, status):

        self.order_id = order_id
        self.customer_id = customer_id
        self.restaurant_id = restaurant_id
        self.order_date = order_date
        self.total_amount = total_amount
        self.status = status

    def display_order(self):

        print("Order ID :", self.order_id)
        print("Customer ID :", self.customer_id)
        print("Restaurant ID :", self.restaurant_id)
        print("Order Date :", self.order_date)
        print("Total Amount :", self.total_amount)
        print("Status :", self.status)