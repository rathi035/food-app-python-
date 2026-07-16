from config.database import get_connection
from models.restaurant import Restaurant
from exceptions.restaurant_exception import RestaurantException


class RestaurantService:

    def add_restaurant(self, restaurant):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            query = "INSERT INTO restaurant (restaurant_id, restaurant_name, location, phone) VALUES (%s, %s, %s, %s)"

            cursor.execute(
                query,
                (
                    restaurant.restaurant_id,
                    restaurant.restaurant_name,
                    restaurant.location,
                    restaurant.phone
                )
            )

            connection.commit()

            print("Restaurant Added Successfully.")

        except Exception as e:

            raise RestaurantException(str(e))

        finally:

            cursor.close()
            connection.close()


    def view_all_restaurants(self):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            query = "SELECT * FROM restaurant"

            cursor.execute(query)

            restaurants = cursor.fetchall()

            if not restaurants:
                raise RestaurantException("No Restaurants Found")

            return restaurants

        except Exception as e:

            raise RestaurantException(str(e))

        finally:

            cursor.close()
            connection.close()


    def update_restaurant(self, restaurant):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            query = "UPDATE restaurant SET restaurant_name=%s, location=%s, phone=%s WHERE restaurant_id=%s"

            cursor.execute(
                query,
                (
                    restaurant.restaurant_name,
                    restaurant.location,
                    restaurant.phone,
                    restaurant.restaurant_id
                )
            )

            if cursor.rowcount == 0:
                raise RestaurantException("Restaurant Not Found")

            connection.commit()

            print("Restaurant Updated Successfully.")

        except Exception as e:

            raise RestaurantException(str(e))

        finally:

            cursor.close()
            connection.close()


    def delete_restaurant(self, restaurant_id):

        connection = get_connection()
        cursor = connection.cursor()

        try:

            query = "DELETE FROM restaurant WHERE restaurant_id=%s"

            cursor.execute(query, (restaurant_id,))

            if cursor.rowcount == 0:
                raise RestaurantException("Restaurant Not Found")

            connection.commit()

            print("Restaurant Deleted Successfully.")

        except Exception as e:

            raise RestaurantException(str(e))

        finally:

            cursor.close()
            connection.close()