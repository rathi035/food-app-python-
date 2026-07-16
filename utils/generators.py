import random
import string


class Generator:

    @staticmethod
    def generate_user_id():

        return random.randint(1000, 9999)


    @staticmethod
    def generate_order_id():

        return random.randint(10000, 99999)


    @staticmethod
    def generate_payment_id():

        return random.randint(100000, 999999)


    @staticmethod
    def generate_customer_id():

        return random.randint(1000, 9999)


    @staticmethod
    def generate_restaurant_id():

        return random.randint(100, 999)


    @staticmethod
    def generate_food_id():

        return random.randint(1000, 9999)


    @staticmethod
    def generate_random_password(length=8):

        characters = string.ascii_letters + string.digits + "@#$%&*"

        return "".join(random.choice(characters) for _ in range(length))