from config.database import get_connection
from models.order_item import OrderItem
from exceptions.order_exception import OrderException


class OrderItemService:

    def add_order_item(self, order_item):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            query = "INSERT INTO order_item (order_item_id, order_id, food_id, quantity, subtotal) VALUES (%s, %s, %s, %s, %s)"

            cursor.execute(
                query,
                (
                    order_item.order_item_id,
                    order_item.order_id,
                    order_item.food_id,
                    order_item.quantity,
                    order_item.subtotal
                )
            )

            connection.commit()

            print("Order Item Added Successfully.")

        except Exception as e:

            raise OrderException(str(e))

        finally:

            cursor.close()
            connection.close()


    def view_all_order_items(self):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            query = "SELECT * FROM order_item"

            cursor.execute(query)

            order_items = cursor.fetchall()

            if not order_items:
                raise OrderException("No Order Items Found")

            return order_items

        except Exception as e:

            raise OrderException(str(e))

        finally:

            cursor.close()
            connection.close()


    def update_order_item(self, order_item):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            query = "UPDATE order_item SET order_id=%s, food_id=%s, quantity=%s, subtotal=%s WHERE order_item_id=%s"

            cursor.execute(
                query,
                (
                    order_item.order_id,
                    order_item.food_id,
                    order_item.quantity,
                    order_item.subtotal,
                    order_item.order_item_id
                )
            )

            if cursor.rowcount == 0:
                raise OrderException("Order Item Not Found")

            connection.commit()

            print("Order Item Updated Successfully.")

        except Exception as e:

            raise OrderException(str(e))

        finally:

            cursor.close()
            connection.close()


    def delete_order_item(self, order_item_id):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            query = "DELETE FROM order_item WHERE order_item_id=%s"

            cursor.execute(query, (order_item_id,))

            if cursor.rowcount == 0:
                raise OrderException("Order Item Not Found")

            connection.commit()

            print("Order Item Deleted Successfully.")

        except Exception as e:

            raise OrderException(str(e))

        finally:

            cursor.close()
            connection.close()