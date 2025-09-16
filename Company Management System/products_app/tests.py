from django.core.exceptions import ValidationError
from django.test import TestCase

from .models import Product
from vendors_app.models import Vendor
from .forms import ProductCreateForm

class ProductCreationTest(TestCase):
    def setUp(self):
        self.vendor_obj = Vendor.objects.create(
            first_name="Pavel",
            last_name="Kalchishkov",
            phone_number="1231231231",
            email="pavel@abv.bg",
            job_title="Manager"
        )

    def test_successful_creation(self):
        form_data = {
            "name": "Laptop",
            "price": 25.50,
            "length": 10,
            "weight": 10,
            "color": "red",
            "vendor": self.vendor_obj.id,
        }
        form = ProductCreateForm(data=form_data)
        self.assertTrue(form.is_valid())

class ProductPriceValidationTest(TestCase):
    def setUp(self):
        self.vendor_obj = Vendor.objects.create(
            first_name="Ivan",
            last_name="Petrov",
            phone_number="1231231231",
            email="ivan@abv.bg",
            job_title="Sales"
        )

        self.product_obj = Product.objects.create(
            name="Phone",
            price=-50,
            length=5,
            weight=2,
            color="black",
            vendor=self.vendor_obj
        )

    def test_negative_price_not_allowed(self):
        self.assertRaises(ValidationError, self.product_obj.full_clean)

class ProductMissingColorTest(TestCase):
    def setUp(self):
        self.vendor_obj = Vendor.objects.create(
            first_name="Ivan",
            last_name="Petrov",
            phone_number="1231231231",
            email="ivan@abv.bg",
            job_title="Sales"
        )

        self.product_obj = Product.objects.create(
            name="Phone",
            price=50,
            length=5,
            weight=2,
            color="",
            vendor=self.vendor_obj
        )

    def test_missing_color(self):
        self.assertRaises(ValidationError, self.product_obj.full_clean)

class ProductIncorrectVendorTest(TestCase):
    def test_wrong_vendor(self):
        with self.assertRaises(ValueError):
            Product.objects.create(
                name="Phone",
                price=50,
                length=5,
                weight=2,
                color="red",
                vendor="NotRealVendor"
            )