from config.database import get_connection
from models.food import Food
from exceptions.food_exception import FoodException


class FoodService:

    def add_food(self, food):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            query = "INSERT INTO food (food_id, food_name, price, category, restaurant_id) VALUES (%s, %s, %s, %s, %s)"

            cursor.execute(
                query,
                (
                    food.food_id,
                    food.food_name,
                    food.price,
                    food.category,
                    food.restaurant_id
                )
            )

            connection.commit()

            print("Food Added Successfully.")

        except Exception as e:

            raise FoodException(str(e))

        finally:

            cursor.close()
            connection.close()


    def view_all_food(self):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            query = "SELECT * FROM food"

            cursor.execute(query)

            foods = cursor.fetchall()

            if not foods:
                raise FoodException("No Food Items Found")

            return foods

        except Exception as e:

            raise FoodException(str(e))

        finally:

            cursor.close()
            connection.close()


    def update_food(self, food):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            query = "UPDATE food SET food_name=%s, price=%s, category=%s, restaurant_id=%s WHERE food_id=%s"

            cursor.execute(
                query,
                (
                    food.food_name,
                    food.price,
                    food.category,
                    food.restaurant_id,
                    food.food_id
                )
            )

            if cursor.rowcount == 0:
                raise FoodException("Food Item Not Found")

            connection.commit()

            print("Food Updated Successfully.")

        except Exception as e:

            raise FoodException(str(e))

        finally:

            cursor.close()
            connection.close()


    def delete_food(self, food_id):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            query = "DELETE FROM food WHERE food_id=%s"

            cursor.execute(query, (food_id,))

            if cursor.rowcount == 0:
                raise FoodException("Food Item Not Found")

            connection.commit()

            print("Food Deleted Successfully.")

        except Exception as e:

            raise FoodException(str(e))

        finally:

            cursor.close()
            connection.close()