import unittest

from services.order_service import OrderService


class TestOrder(unittest.TestCase):

    def test_view_all_orders(self):

        service = OrderService()

        orders = service.view_all_orders()

        print("\nOrders:")
        for order in orders:
            print(order)

        self.assertGreater(len(orders), 0)


if __name__ == "__main__":
    unittest.main()