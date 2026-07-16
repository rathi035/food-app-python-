from config.database import get_connection
from models.customer import Customer
from exceptions.customer_exception import CustomerException


class CustomerService:

    def add_customer(self, customer):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            query = "INSERT INTO customer (customer_id, user_id, name, email, phone, address) VALUES (%s, %s, %s, %s, %s, %s)"

            cursor.execute(
                query,
                (
                    customer.customer_id,
                    customer.user_id,
                    customer.name,
                    customer.email,
                    customer.phone,
                    customer.address
                )
            )

            connection.commit()

            print("Customer Added Successfully.")

        except Exception as e:

            raise CustomerException(str(e))

        finally:

            cursor.close()
            connection.close()


    def view_all_customers(self):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            query = "SELECT * FROM customer"

            cursor.execute(query)

            customers = cursor.fetchall()

            if not customers:
                raise CustomerException("No Customers Found")

            return customers

        except Exception as e:

            raise CustomerException(str(e))

        finally:

            cursor.close()
            connection.close()


    def update_customer(self, customer):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            query = "UPDATE customer SET user_id=%s, name=%s, email=%s, phone=%s, address=%s WHERE customer_id=%s"

            cursor.execute(
                query,
                (
                    customer.user_id,
                    customer.name,
                    customer.email,
                    customer.phone,
                    customer.address,
                    customer.customer_id
                )
            )

            if cursor.rowcount == 0:
                raise CustomerException("Customer Not Found")

            connection.commit()

            print("Customer Updated Successfully.")

        except Exception as e:

            raise CustomerException(str(e))

        finally:

            cursor.close()
            connection.close()


    def delete_customer(self, customer_id):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            query = "DELETE FROM customer WHERE customer_id=%s"

            cursor.execute(
                query,
                (customer_id,)
            )

            if cursor.rowcount == 0:
                raise CustomerException("Customer Not Found")

            connection.commit()

            print("Customer Deleted Successfully.")

        except Exception as e:

            raise CustomerException(str(e))

        finally:

            cursor.close()
            connection.close()