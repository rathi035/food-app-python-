class Customer:
    
    def __init__(self, customer_id,user_id, name, email,phone,address):
        self.customer_id = customer_id
        self.user_id = user_id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        
    def display_customer(self):
        
        print("Customer ID :", self.customer_id)
        print("User ID :", self.user_id)
        print("Name :", self.name)
        print("Email :", self.email)
        print("Phone :", self.phone)
        print("Address :", self.address)