from config.database import get_connection
from models.user import User
from exceptions.user_exception import UserException


class UserService:

    def add_user(self, user):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            query = """
            INSERT INTO users (user_id, username, password, role)
            VALUES (%s, %s, %s, %s)
            """

            cursor.execute(
                query,
                (
                    user.user_id,
                    user.username,
                    user.password,
                    user.role
                )
            )

            connection.commit()

            print("User Added Successfully.")

        except Exception as e:

            raise UserException(str(e))

        finally:

            cursor.close()
            connection.close()

    def view_all_users(self):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            query = "SELECT * FROM users"

            cursor.execute(query)

            users = cursor.fetchall()

            if not users:
                raise UserException("No Users Found")

            return users

        except Exception as e:

            raise UserException(str(e))

        finally:

            cursor.close()
            connection.close()

    def update_user(self, user):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            query = """
            UPDATE users
            SET username=%s,
                password=%s,
                role=%s
            WHERE user_id=%s
            """

            print("\n----- DEBUG -----")
            print("User ID :", user.user_id)
            print("Username :", user.username)
            print("Password :", user.password)
            print("Role :", user.role)

            cursor.execute(
                query,
                (
                    user.username,
                    user.password,
                    user.role,
                    user.user_id
                )
            )

            print("Rows Updated :", cursor.rowcount)

            if cursor.rowcount == 0:
                raise UserException("User Not Found")

            connection.commit()

            print("User Updated Successfully.")

        except Exception as e:

            raise UserException(str(e))

        finally:

            cursor.close()
            connection.close()

    def delete_user(self, user_id):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            query = "DELETE FROM users WHERE user_id=%s"

            cursor.execute(query, (user_id,))

            if cursor.rowcount == 0:
                raise UserException("User Not Found")

            connection.commit()

            print("User Deleted Successfully.")

        except Exception as e:

            raise UserException(str(e))

        finally:

            cursor.close()
            connection.close()

    def login(self, username, password):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            query = """
            SELECT * FROM users
            WHERE username=%s AND password=%s
            """

            cursor.execute(query, (username, password))

            user = cursor.fetchone()

            if not user:
                raise UserException("Invalid Username or Password")

            return user

        except Exception as e:

            raise UserException(str(e))

        finally:

            cursor.close()
            connection.close()