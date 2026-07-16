from config.database import get_connection
from models.payment import Payment
from exceptions.payment_exception import PaymentException


class PaymentService:

    def add_payment(self, payment):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            query = "INSERT INTO payment (payment_id, order_id, amount, payment_method, payment_status) VALUES (%s, %s, %s, %s, %s)"

            cursor.execute(
                query,
                (
                    payment.payment_id,
                    payment.order_id,
                    payment.amount,
                    payment.payment_method,
                    payment.payment_status
                )
            )

            connection.commit()

            print("Payment Added Successfully.")

        except Exception as e:

            raise PaymentException(str(e))

        finally:

            cursor.close()
            connection.close()


    def view_all_payments(self):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            query = "SELECT * FROM payment"

            cursor.execute(query)

            payments = cursor.fetchall()

            if not payments:
                raise PaymentException("No Payments Found")

            return payments

        except Exception as e:

            raise PaymentException(str(e))

        finally:

            cursor.close()
            connection.close()


    def update_payment(self, payment):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            query = "UPDATE payment SET order_id=%s, amount=%s, payment_method=%s, payment_status=%s WHERE payment_id=%s"

            cursor.execute(
                query,
                (
                    payment.order_id,
                    payment.amount,
                    payment.payment_method,
                    payment.payment_status,
                    payment.payment_id
                )
            )

            if cursor.rowcount == 0:
                raise PaymentException("Payment Not Found")

            connection.commit()

            print("Payment Updated Successfully.")

        except Exception as e:

            raise PaymentException(str(e))

        finally:

            cursor.close()
            connection.close()


    def delete_payment(self, payment_id):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            query = "DELETE FROM payment WHERE payment_id=%s"

            cursor.execute(query, (payment_id,))

            if cursor.rowcount == 0:
                raise PaymentException("Payment Not Found")

            connection.commit()

            print("Payment Deleted Successfully.")

        except Exception as e:

            raise PaymentException(str(e))

        finally:

            cursor.close()
            connection.close()