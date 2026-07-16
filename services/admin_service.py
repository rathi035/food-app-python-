from config.database import get_connection


class AdminService:

    def view_all_users(self):

        connection = get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM users"

        cursor.execute(query)

        users = cursor.fetchall()

        cursor.close()
        connection.close()

        return users


    def view_all_customers(self):

        connection = get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM customer"

        cursor.execute(query)

        customers = cursor.fetchall()

        cursor.close()
        connection.close()

        return customers


    def view_all_restaurants(self):

        connection = get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM restaurant"

        cursor.execute(query)

        restaurants = cursor.fetchall()

        cursor.close()
        connection.close()

        return restaurants


    def view_all_orders(self):

        connection = get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM orders"

        cursor.execute(query)

        orders = cursor.fetchall()

        cursor.close()
        connection.close()

        return orders