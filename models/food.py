class Food:
    
    def __init__(self, food_id, food_name, price, category, restaurant_id):
        self.food_id = food_id
        self.food_name = food_name
        self.price = price
        self.category = category
        self.restaurant_id = restaurant_id

    def display_food(self):

        print("Food ID :", self.food_id)
        print("Food Name :", self.food_name)
        print("Price :", self.price)
        print("Category :", self.category)
        print("Restaurant ID :", self.restaurant_id)