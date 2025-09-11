from django.core.exceptions import ValidationError
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Vendor
User = get_user_model()


class ShipperModelCreationTest(TestCase):
    def setUp(self):
        self.vendor_obj = Vendor.objects.create(
            first_name="Pavel",
            last_name="Kalchishkov",
            phone_number="1231231231",
            email="pavel@abv.bg",
            job_title="Manager"
        )
        self.vendor_obj.full_clean()
        self.vendor_obj.save()

    def test_successful_creation(self):
        self.assertEqual(str(self.vendor_obj), "Pavel Kalchishkov")


class VendorIncorrectPhoneNumberCharactersTest(TestCase):
    def setUp(self):
        self.vendor_obj = Vendor.objects.create(
            first_name="Pavel",
            last_name="Kalchishkov",
            phone_number="123123123a",
            email="pavel@abv.bg",
            job_title="Manager"
        )

    def test_creation_with_incorrect_phone_number_characters(self):
        self.assertRaises(ValidationError, self.vendor_obj.full_clean)


class VendorIncorrectPhoneNumberLengthTest(TestCase):
    def setUp(self):
        self.vendor_obj = Vendor.objects.create(
            first_name="Pavel",
            last_name="Kalchishkov",
            phone_number="12312312311",
            email="pavel@abv.bg",
            job_title="Manager"
        )

    def test_creation_with_larger_phone_number(self):
        self.assertRaises(ValidationError, self.vendor_obj.full_clean)


class VendorEmailRequiredTest(TestCase):
    def setUp(self):
        self.vendor_obj = Vendor.objects.create(
            first_name="Pavel",
            last_name="Kalchishkov",
            phone_number="1231231231",
            email="",  # missing email
            job_title="Manager"
        )

    def test_email_is_required(self):
        self.assertRaises(ValidationError, self.vendor_obj.full_clean)


