from models.customer import Customer
from models.restaurant import Restaurant
from models.food import Food
from models.order import Order
from models.order_item import OrderItem
from models.payment import Payment
from models.user import User
from utils.logs import Logger

from utils.jwt_manager import JWTManager

from services.customer_service import CustomerService
from services.restaurant_service import RestaurantService
from services.food_service import FoodService
from services.order_service import OrderService
from services.order_item_service import OrderItemService
from services.payment_service import PaymentService
from services.user_service import UserService
from utils.validators import Validator
from exceptions.customer_exception import CustomerException
from exceptions.restaurant_exception import RestaurantException
from exceptions.food_exception import FoodException
from exceptions.order_exception import OrderException
from exceptions.payment_exception import PaymentException
from exceptions.user_exception import UserException

customer_service = CustomerService()
restaurant_service = RestaurantService()
food_service = FoodService()
order_service = OrderService()
order_item_service = OrderItemService()
payment_service = PaymentService()
user_service = UserService()
jwt_manager = JWTManager()

while True:

    print("\n Food Delivery Management System:")
    print("1. Customer")
    print("2. Restaurant")
    print("3. Food")
    print("4. Order")
    print("5. Order Item")
    print("6. Payment")
    print("7. User")
    print("8. Exit")

    choice = int(input("Enter your choice : "))

    if choice == 1:

        while True:

            print("\n Customer Menu:")
            print("1. Add Customer")
            print("2. View All Customers")
            print("3. Update Customer")
            print("4. Delete Customer")
            print("5. Back")

            customer_choice = int(input("Enter your choice : "))

            if customer_choice == 1:

                customer_id = int(input("Enter Customer ID : "))
                user_id = int(input("Enter User ID : "))
                name = input("Enter Name : ")
                email = input("Enter Email : ")
                if not Validator.validate_email(email):
                    print("Invalid Email! Please enter a valid email address.")
                    continue
                phone = input("Enter Phone : ")
                if not Validator.validate_phone(phone):
                    print("Invalid Phone! Please enter a valid 10-digit phone number starting with 6, 7, 8, or 9.")
                    continue
                phone = int(phone)
                address = input("Enter Address : ")

                customer = Customer(
                    customer_id,
                    user_id,
                    name,
                    email,
                    phone,
                    address
                )

                try:
                    customer_service.add_customer(customer)
                except CustomerException as e:
                    Logger.error(e)

            elif customer_choice == 2:

                try:

                    customers = customer_service.view_all_customers()

                    for customer in customers:
                        print(customer)

                except CustomerException as e:
                    print(e)

            elif customer_choice == 3:

                customer_id = int(input("Enter Customer ID : "))
                user_id = int(input("Enter User ID : "))
                name = input("Enter New Name : ")
                email = input("Enter New Email : ")
                if not Validator.validate_email(email):
                    print("Invalid Email! Please enter a valid email address.")
                    continue
                phone = input("Enter New Phone : ")
                if not Validator.validate_phone(phone):
                    print("Invalid Phone! Please enter a valid 10-digit phone number starting with 6, 7, 8, or 9.")
                    continue
                phone = int(phone)
                address = input("Enter New Address : ")

                customer = Customer(
                    customer_id,
                    user_id,
                    name,
                    email,
                    phone,
                    address
                )

                try:
                    customer_service.update_customer(customer)
                except CustomerException as e:
                    print(e)

            elif customer_choice == 4:

                customer_id = int(input("Enter Customer ID : "))

                try:
                    customer_service.delete_customer(customer_id)
                except CustomerException as e:
                    print(e)

            elif customer_choice == 5:

                break

            else:

                print("Invalid Choice.")
    elif choice == 2:
    
        while True:

            print("\n Restaurant Menu:")
            print("1. Add Restaurant")
            print("2. View All Restaurants")
            print("3. Update Restaurant")
            print("4. Delete Restaurant")
            print("5. Back")

            restaurant_choice = int(input("Enter your choice : "))

            if restaurant_choice == 1:

                restaurant_id = int(input("Enter Restaurant ID : "))
                restaurant_name = input("Enter Restaurant Name : ")
                location = input("Enter Location : ")
                phone = input("Enter Phone : ")

                if not Validator.validate_phone(phone):
                    print("Invalid Phone! Please enter a valid 10-digit phone number starting with 6, 7, 8, or 9.")
                    continue

                restaurant = Restaurant(
                    restaurant_id,
                    restaurant_name,
                    location,
                    phone
                )

                try:
                    restaurant_service.add_restaurant(restaurant)
                except RestaurantException as e:
                    print(e)

            elif restaurant_choice == 2:

                try:

                    restaurants = restaurant_service.view_all_restaurants()

                    for restaurant in restaurants:
                        print(restaurant)

                except RestaurantException as e:
                    print(e)

            elif restaurant_choice == 3:

                restaurant_id = int(input("Enter Restaurant ID : "))
                restaurant_name = input("Enter Restaurant Name : ")
                location = input("Enter Location : ")
                phone = input("Enter Phone : ")
                if not Validator.validate_phone(phone):
                    print("Invalid Phone! Please enter a valid 10-digit phone number starting with 6, 7, 8, or 9.")
                    continue
                phone = int(phone)

                restaurant = Restaurant(
                    restaurant_id,
                    restaurant_name,
                    location,
                    phone
                )

                try:
                    restaurant_service.update_restaurant(restaurant)
                except RestaurantException as e:
                    print(e)

            elif restaurant_choice == 4:

                restaurant_id = int(input("Enter Restaurant ID : "))

                try:
                    restaurant_service.delete_restaurant(restaurant_id)
                except RestaurantException as e:
                    print(e)

            elif restaurant_choice == 5:

                break

            else:

                print("Invalid Choice.")

    elif choice == 3:

        while True:

            print("\n Food Menu:")
            print("1. Add Food")
            print("2. View All Foods")
            print("3. Update Food")
            print("4. Delete Food")
            print("5. Back")

            food_choice = int(input("Enter your choice : "))

            if food_choice == 1:

                food_id = int(input("Enter Food ID : "))
                food_name = input("Enter Food Name : ")
                price = float(input("Enter Price : "))
                category = input("Enter Category : ")
                restaurant_id = int(input("Enter Restaurant ID : "))

                food = Food(
                    food_id,
                    food_name,
                    price,
                    category,
                    restaurant_id
                )

                try:
                    food_service.add_food(food)
                except FoodException as e:
                    print(e)

            elif food_choice == 2:

                try:

                    foods = food_service.view_all_food()

                    for food in foods:
                        print(food)

                except FoodException as e:
                    print(e)

            elif food_choice == 3:

                food_id = int(input("Enter Food ID : "))
                food_name = input("Enter Food Name : ")
                price = float(input("Enter Price : "))
                category = input("Enter Category : ")
                restaurant_id = int(input("Enter Restaurant ID : "))

                food = Food(
                    food_id,
                    food_name,
                    price,
                    category,
                    restaurant_id
                )

                try:
                    food_service.update_food(food)
                except FoodException as e:
                    print(e)

            elif food_choice == 4:

                food_id = int(input("Enter Food ID : "))

                try:
                    food_service.delete_food(food_id)
                except FoodException as e:
                    print(e)

            elif food_choice == 5:

                break

            else:

                print("Invalid Choice.")
    elif choice == 4:
    
        while True:

            print("\n Order Menu:")
            print("1. Add Order")
            print("2. View All Orders")
            print("3. Update Order")
            print("4. Delete Order")
            print("5. Back")

            order_choice = int(input("Enter your choice : "))

            if order_choice == 1:

                order_id = int(input("Enter Order ID : "))
                customer_id = int(input("Enter Customer ID : "))
                restaurant_id = int(input("Enter Restaurant ID : "))
                order_date = input("Enter Order Date (YYYY-MM-DD) : ")
                total_amount = float(input("Enter Total Amount : "))
                status = input("Enter Status : ")

                order = Order(
                    order_id,
                    customer_id,
                    restaurant_id,
                    order_date,
                    total_amount,
                    status
                )

                try:
                    order_service.add_order(order)
                except OrderException as e:
                    print(e)

            elif order_choice == 2:

                try:

                    orders = order_service.view_all_orders()

                    for order in orders:
                        print(order)

                except OrderException as e:
                    print(e)

            elif order_choice == 3:

                order_id = int(input("Enter Order ID : "))
                customer_id = int(input("Enter Customer ID : "))
                restaurant_id = int(input("Enter Restaurant ID : "))
                order_date = input("Enter Order Date : ")
                total_amount = float(input("Enter Total Amount : "))
                status = input("Enter Status : ")

                order = Order(
                    order_id,
                    customer_id,
                    restaurant_id,
                    order_date,
                    total_amount,
                    status
                )

                try:
                    order_service.update_order(order)
                except OrderException as e:
                    print(e)

            elif order_choice == 4:

                order_id = int(input("Enter Order ID : "))

                try:
                    order_service.delete_order(order_id)
                except OrderException as e:
                    print(e)

            elif order_choice == 5:

                break

            else:

                print("Invalid Choice.")

    elif choice == 5:

        while True:

            print("\n Order Item Menu:")
            print("1. Add Order Item")
            print("2. View All Order Items")
            print("3. Update Order Item")
            print("4. Delete Order Item")
            print("5. Back")

            order_item_choice = int(input("Enter your choice : "))

            if order_item_choice == 1:

                order_item_id = int(input("Enter Order Item ID : "))
                order_id = int(input("Enter Order ID : "))
                food_id = int(input("Enter Food ID : "))
                quantity = int(input("Enter Quantity : "))
                subtotal = float(input("Enter Subtotal : "))

                order_item = OrderItem(
                    order_item_id,
                    order_id,
                    food_id,
                    quantity,
                    subtotal
                )

                try:
                    order_item_service.add_order_item(order_item)
                except OrderException as e:
                    print(e)

            elif order_item_choice == 2:

                try:

                    order_items = order_item_service.view_all_order_items()

                    for item in order_items:
                        print(item)

                except OrderException as e:
                    print(e)

            elif order_item_choice == 3:

                order_item_id = int(input("Enter Order Item ID : "))
                order_id = int(input("Enter Order ID : "))
                food_id = int(input("Enter Food ID : "))
                quantity = int(input("Enter Quantity : "))
                subtotal = float(input("Enter Subtotal : "))

                order_item = OrderItem(
                    order_item_id,
                    order_id,
                    food_id,
                    quantity,
                    subtotal
                )

                try:
                    order_item_service.update_order_item(order_item)
                except OrderException as e:
                    print(e)

            elif order_item_choice == 4:

                order_item_id = int(input("Enter Order Item ID : "))

                try:
                    order_item_service.delete_order_item(order_item_id)
                except OrderException as e:
                    print(e)

            elif order_item_choice == 5:

                break

            else:

                print("Invalid Choice.")
    elif choice == 6:
    
        while True:

            print("\n Payment Menu:")
            print("1. Add Payment")
            print("2. View All Payments")
            print("3. Update Payment")
            print("4. Delete Payment")
            print("5. Back")

            payment_choice = int(input("Enter your choice : "))

            if payment_choice == 1:

                payment_id = int(input("Enter Payment ID : "))
                order_id = int(input("Enter Order ID : "))
                amount = float(input("Enter Amount : "))
                payment_method = input("Enter Payment Method : ")
                payment_status = input("Enter Payment Status : ")

                payment = Payment(
                    payment_id,
                    order_id,
                    amount,
                    payment_method,
                    payment_status
                )

                try:
                    payment_service.add_payment(payment)
                except PaymentException as e:
                    print(e)

            elif payment_choice == 2:

                try:

                    payments = payment_service.view_all_payments()

                    for payment in payments:
                        print(payment)

                except PaymentException as e:
                    print(e)

            elif payment_choice == 3:

                payment_id = int(input("Enter Payment ID : "))
                order_id = int(input("Enter Order ID : "))
                amount = float(input("Enter Amount : "))
                payment_method = input("Enter Payment Method : ")
                payment_status = input("Enter Payment Status : ")

                payment = Payment(
                    payment_id,
                    order_id,
                    amount,
                    payment_method,
                    payment_status
                )

                try:
                    payment_service.update_payment(payment)
                except PaymentException as e:
                    print(e)

            elif payment_choice == 4:

                payment_id = int(input("Enter Payment ID : "))

                try:
                    payment_service.delete_payment(payment_id)
                except PaymentException as e:
                    print(e)

            elif payment_choice == 5:

                break

            else:

                print("Invalid Choice.")

    elif choice == 7:

        while True:

            print("\n User Menu:")
            print("1. Add User")
            print("2. View All Users")
            print("3. Update User")
            print("4. Delete User")
            print("5. Login")
            print("6. Back")

            user_choice = int(input("Enter your choice : "))

            if user_choice == 1:
    
                user_id = int(input("Enter User ID : "))

                username = input("Enter Username : ")

                if not Validator.validate_username(username):
                    print("Invalid Username! Username must start with a letter and contain at least 3 characters.")
                    continue

                password = input("Enter Password : ")

                if not Validator.validate_password(password):
                    print("Invalid Password! Password must be at least 6 characters with at least one letter and one number.")
                    continue

                role = input("Enter Role : ").lower()
                if not Validator.validate_role(role):
                    print("Invalid Role! Role must be either 'admin' or 'customer'.")
                    continue

                user = User(
                    user_id,
                    username,
                    password,
                    role
                )

                try:
                    user_service.add_user(user)

                except UserException as e:
                    print(e)
            elif user_choice == 2:

                try:

                    users = user_service.view_all_users()

                    for user in users:
                        print(user)

                except UserException as e:
                    print(e)

            elif user_choice == 3:

                user_id = int(input("Enter User ID : "))
                username = input("Enter Username : ")
                if not Validator.validate_username(username):
                    print("Invalid Username! Username must start with a letter and contain at least 3 characters.")
                    continue
                password = input("Enter Password : ")
                if not Validator.validate_password(password):
                    print("Invalid Password! Password must be at least 6 characters with at least one letter and one number.")
                    continue
                role = input("Enter Role : ").lower()

                if not Validator.validate_role(role):
                    print("Invalid Role! Role must be either 'admin' or 'customer'.")
                    continue

                user = User(
                    user_id,
                    username,
                    password,
                    role
                )

                try:
                    user_service.update_user(user)
                except UserException as e:
                    print(e)

            elif user_choice == 4:

                user_id = int(input("Enter User ID : "))

                try:
                    user_service.delete_user(user_id)
                except UserException as e:
                    print(e)

            elif user_choice == 5:

                username = input("Enter Username : ")
                password = input("Enter Password : ")

                try:

                    user = user_service.login(username, password)

                    token = JWTManager.generate_token(
                        user[0],
                        user[1],
                        user[3]
                    )

                    print("\nLogin Successful.")
                    print("JWT Token :")
                    print(token)

                    payload = JWTManager.verify_token(token)

                    print("\nDecoded Token")
                    print(payload)

                except UserException as e:
                    print(e)

            elif user_choice == 6:

                break

            else:

                print("Invalid Choice.")

    elif choice == 8:

        print("\nThank You for using Food Delivery Management System.")
        break

    else:

        print("Invalid Choice.")
