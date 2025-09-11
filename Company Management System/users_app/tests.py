from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserCreationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="pavel123",
            email="pavel@example.com",
            password="securepassword123",
            phone_number="1234567890"
        )

    def test_user_creation(self):
        self.assertEqual(str(self.user.username), "pavel123")
        self.assertEqual(str(self.user.email), "pavel@example.com")
        self.assertEqual(str(self.user.password), "securepassword123")

class CustomUserIncorrectPasswordTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="pavel123",
            email="pavel@example.com",
            password="",
            phone_number="1234567890"
        )

    def test_user_with_no_password(self):
        self.assertRaises(ValidationError, self.user.full_clean)

class CustomUserIncorrectEmailTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="pavel123",
            email="",
            password="password909",
            phone_number="1234567890"
        )


    def test_user_with_no_email(self):
        self.assertRaises(ValidationError, self.user.full_clean)

