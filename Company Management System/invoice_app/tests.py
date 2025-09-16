from django.test import TestCase
from decimal import Decimal
from .models import Company, Invoice
from orders_app.models import Order
from clients_app.models import Client
from employees_app.models import Employee
from shippers_app.models import Shipper


class CompanyModelTests(TestCase):
    def setUp(self):
        self.company = Company.objects.create(
            eik="1234567890123",
            dds="BG123456789",
            name="AgroCompany Ltd.",
            address="Sofia, Bulgaria",
            mol="Ivan Ivanov",
            recipient="AgroCompany Warehouse"
        )

    def test_company_creation(self):
        self.assertTrue(isinstance(self.company, Company))
        self.assertEqual(str(self.company), f"{self.company.eik} - {self.company.name}")

    def test_update_company_name(self):
        self.company.name = "New AgroCompany"
        self.company.save()
        updated_company = Company.objects.get(id=self.company.id)
        self.assertEqual(updated_company.name, "New AgroCompany")


class InvoiceModelTests(TestCase):
    def setUp(self):
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
        self.company = Company.objects.create(
            eik="9876543210123",
            dds="BG987654321",
            name="Farmers Group",
            address="Plovdiv, Bulgaria",
            mol="Petar Petrov",
            recipient="Farmers Storage"
        )
        self.order = Order.objects.create(
            order_address="Varna, Bulgaria",
            order_price=Decimal("1000.00"),
            client=self.client,
            employee=self.employee,
            shipper=self.shipper
        )
        self.invoice = Invoice.objects.create(
            company=self.company,
            order=self.order,
            DDS="20",
            discount=Decimal("10.00"),
            whole_price_without_dds=Decimal("1000.00"),
            whole_price_with_dds=Decimal("1200.00"),
            comment="Initial invoice"
        )

    def test_invoice_creation(self):
        self.assertTrue(isinstance(self.invoice, Invoice))
        self.assertEqual(str(self.invoice), f"No.{self.invoice.id}")
        self.assertEqual(self.invoice.company.name, "Farmers Group")
        self.assertEqual(self.invoice.order.client.first_name, "Pavel")

    def test_invoice_default_values(self):
        invoice2 = Invoice.objects.create(company=self.company, order=self.order)
        self.assertEqual(invoice2.DDS, "20")
        self.assertEqual(invoice2.discount, Decimal("0"))
        self.assertFalse(invoice2.cancelled)

    def test_cancel_invoice(self):
        self.invoice.cancelled = True
        self.invoice.save()
        cancelled_invoice = Invoice.objects.get(id=self.invoice.id)
        self.assertTrue(cancelled_invoice.cancelled)
