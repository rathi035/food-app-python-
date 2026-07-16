import unittest

from services.food_service import FoodService


class TestFood(unittest.TestCase):

    def test_view_all_food(self):

        service = FoodService()

        foods = service.view_all_food()

        print("\nFood Items:")
        for food in foods:
            print(food)

        self.assertGreater(len(foods), 0)


if __name__ == "__main__":
    unittest.main()