from config.database import get_connection
from models.order import Order
from exceptions.order_exception import OrderException


class OrderService:

    def add_order(self, order):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            query = "INSERT INTO orders (order_id, customer_id, restaurant_id, order_date, total_amount, status) VALUES (%s, %s, %s, %s, %s, %s)"

            cursor.execute(
                query,
                (
                    order.order_id,
                    order.customer_id,
                    order.restaurant_id,
                    order.order_date,
                    order.total_amount,
                    order.status
                )
            )

            connection.commit()

            print("Order Added Successfully.")

        except Exception as e:

            raise OrderException(str(e))

        finally:

            cursor.close()
            connection.close()


    def view_all_orders(self):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            query = "SELECT * FROM orders"

            cursor.execute(query)

            orders = cursor.fetchall()

            if not orders:
                raise OrderException("No Orders Found")

            return orders

        except Exception as e:

            raise OrderException(str(e))

        finally:

            cursor.close()
            connection.close()


    def update_order(self, order):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            query = "UPDATE orders SET customer_id=%s, restaurant_id=%s, order_date=%s, total_amount=%s, status=%s WHERE order_id=%s"

            cursor.execute(
                query,
                (
                    order.customer_id,
                    order.restaurant_id,
                    order.order_date,
                    order.total_amount,
                    order.status,
                    order.order_id
                )
            )

            if cursor.rowcount == 0:
                raise OrderException("Order Not Found")

            connection.commit()

            print("Order Updated Successfully.")

        except Exception as e:

            raise OrderException(str(e))

        finally:

            cursor.close()
            connection.close()


    def delete_order(self, order_id):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            query = "DELETE FROM orders WHERE order_id=%s"

            cursor.execute(query, (order_id,))

            if cursor.rowcount == 0:
                raise OrderException("Order Not Found")

            connection.commit()

            print("Order Deleted Successfully.")

        except Exception as e:

            raise OrderException(str(e))

        finally:

            cursor.close()
            connection.close()