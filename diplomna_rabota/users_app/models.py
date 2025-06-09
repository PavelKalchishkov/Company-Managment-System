from django.db import models
from django.contrib.auth.models import AbstractUser
from common.validators import AllNumbersValidator, TenCharactersValidator

class CustomUser(AbstractUser):
    username = models.CharField(max_length=10,
                                unique=True,
                                help_text={
                                    'unique': "A user with that username already exists.",
                                    'max_length': "The user's username must be 10 characters or less.",
                                })

    phone_number = models.CharField(max_length=100,
                                    validators=[AllNumbersValidator,
                                                TenCharactersValidator])

    email = models.EmailField(unique=True,max_length=30)