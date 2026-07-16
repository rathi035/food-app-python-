class Restaurant:
    
    def __init__(self, restaurant_id, restaurant_name, location, phone):

        self.restaurant_id = restaurant_id
        self.restaurant_name = restaurant_name
        self.location = location
        self.phone = phone

    def display_restaurant(self):

        print("Restaurant ID :", self.restaurant_id)
        print("Restaurant Name :", self.restaurant_name)
        print("Location :", self.location)
        print("Phone :", self.phone)