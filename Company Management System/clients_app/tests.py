from django.core.exceptions import ValidationError
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Client
User = get_user_model()
from invoice_app.models import Company

class ClientCreationTest(TestCase):
    def setUp(self):
        self.client_obj = Client.objects.create(
            first_name="Pavel",
            last_name="Kalchishkov",
            phone_number="1231231231",
            email="pavel@abv.bg",
            job_title="Manager"
        )
        self.client_obj.full_clean()
        self.client_obj.save()

    def test_successful_creation_of_client(self):
        self.assertEqual(str(self.client_obj), "Pavel Kalchishkov")


class ClientIncorrectPhoneNumberCharactersTest(TestCase):
    def setUp(self):
        self.client_obj = Client.objects.create(
            first_name="Pavel",
            last_name="Kalchishkov",
            phone_number="123123123a",
            email="pavel@abv.bg",
            job_title="Manager"
        )

    def test_creating_a_client_object(self):
        self.assertRaises(ValidationError, self.client_obj.full_clean)


class ClientIncorrectPhoneNumberLengthTest(TestCase):
    def setUp(self):
        self.client_obj = Client.objects.create(
            first_name="Pavel",
            last_name="Kalchishkov",
            phone_number="12312312311",
            email="pavel@abv.bg",
            job_title="Manager"
        )

    def test_creating_a_client_object(self):
        self.assertRaises(ValidationError, self.client_obj.full_clean)


class ClientEmailRequiredTest(TestCase):
    def setUp(self):
        self.client_obj = Client(
            first_name="Pavel",
            last_name="Kalchishkov",
            phone_number="1231231231",
            email="",  # missing email
            job_title="Manager"
        )

    def test_email_is_required(self):
        self.assertRaises(ValidationError, self.client_obj.full_clean)

class ClientWithCompanyRelationTest(TestCase):
    def setUp(self):
        self.company = Company.objects.create(
            eik="1234567890123",
            dds="BG1234567890123",
            name="RuseOOD",
            address="Ruse",
            mol="123123123123",
            recipient="Pavel Kalchishkov",
        )
        self.client_obj = Client.objects.create(
            first_name="Simeon",
            last_name="Nikolov",
            phone_number="3333333333",
            email="Simeon@abv.bg",
            job_title="Director",
            company=self.company
        )
        self.client_obj.full_clean()
        self.client_obj.save()

    def test_client_is_assigned_to_company(self):
        self.assertEqual(self.client_obj.company.name, "RuseOOD")






