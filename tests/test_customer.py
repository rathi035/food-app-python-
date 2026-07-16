import unittest

from services.customer_service import CustomerService


class TestCustomer(unittest.TestCase):

    def test_view_all_customers(self):

        service = CustomerService()

        customers = service.view_all_customers()

        print("\nCustomers:")
        for customer in customers:
            print(customer)

        self.assertGreater(len(customers), 0)


if __name__ == "__main__":
    unittest.main()