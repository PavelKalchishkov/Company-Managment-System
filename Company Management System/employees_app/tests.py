from django.core.exceptions import ValidationError
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Employee
User = get_user_model()


class EmployeeModelCreationTest(TestCase):
    def setUp(self):
        self.employee_obj = Employee.objects.create(
            first_name="Pavel",
            last_name="Kalchishkov",
            phone_number="1231231231",
            email="pavel@abv.bg",
            job_title="Manager"
        )
        self.employee_obj.full_clean()
        self.employee_obj.save()

    def test_successful_creation_of_employee(self):
        self.assertEqual(str(self.employee_obj), "Pavel Kalchishkov")


class EmployeeIncorrectPhoneNumberCharactersTest(TestCase):
    def setUp(self):
        self.employee_obj = Employee.objects.create(
            first_name="Pavel",
            last_name="Kalchishkov",
            phone_number="123123123a",
            email="pavel@abv.bg",
            job_title="Manager"
        )

    def test_employee_creation_with_incorrect_phone_number_characters(self):
        self.assertRaises(ValidationError, self.employee_obj.full_clean)


class EmployeeIncorrectPhoneNumberLengthTest(TestCase):
    def setUp(self):
        self.employee_obj = Employee.objects.create(
            first_name="Pavel",
            last_name="Kalchishkov",
            phone_number="12312312311",
            email="pavel@abv.bg",
            job_title="Manager"
        )

    def test_employee_creation_with_larger_phone_number(self):
        self.assertRaises(ValidationError, self.employee_obj.full_clean)


class EmployeeEmailRequiredTest(TestCase):
    def setUp(self):
        self.employee_obj = Employee.objects.create(
            first_name="Pavel",
            last_name="Kalchishkov",
            phone_number="1231231231",
            email="",  # missing email
            job_title="Manager"
        )

    def test_email_is_required(self):
        self.assertRaises(ValidationError, self.employee_obj.full_clean)
