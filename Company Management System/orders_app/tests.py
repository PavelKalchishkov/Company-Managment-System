from django.test import TestCase
from decimal import Decimal
from orders_app.models import Order
from products_app.models import Product
from vendors_app.models import Vendor
from clients_app.models import Client
from employees_app.models import Employee
from shippers_app.models import Shipper


class OrderModelTests(TestCase):
    def setUp(self):
        # Vendor needed for Product
        self.vendor = Vendor.objects.create(
            first_name="Vendor",
            last_name="Test",
            phone_number="1234567890",
            email="vendor@test.com",
            job_title="Supplier"
        )

        self.product = Product.objects.create(
            name="Laptop",
            price=1200.00,
            length=15,
            weight=2.5,
            color="Gray",
            vendor=self.vendor
        )

        self.client = Client.objects.create(
            first_name="Pavel",
            last_name="Kalchishkov",
            phone_number="1234567890",
            email="pavel@abv.bg",
            job_title="Manager"
        )

        self.employee = Employee.objects.create(
            first_name="Maria",
            last_name="Ivanova",
            phone_number="1234567890",
            email="maria@company.com",
            job_title="Sales"
        )

        self.shipper = Shipper.objects.create(
            first_name="John",
            last_name="Doe",
            phone_number="1234567890",
            email="john@ship.com",
            job_title="Driver"
        )

        self.order = Order.objects.create(
            order_address="Sofia, Bulgaria",
            order_price=Decimal("1500.00"),
            client=self.client,
            employee=self.employee,
            shipper=self.shipper
        )

    def test_order_creation(self):
        self.assertTrue(isinstance(self.order, Order))
        self.assertEqual(str(self.order), f"PO#{self.order.id}")

    def test_order_default_values(self):
        self.assertEqual(self.order.order_status, "pending")
        self.assertEqual(self.order.payment_method, "cash")

    def test_add_products_to_order(self):
        self.order.products.add(self.product)
        self.assertIn(self.product, self.order.products.all())

