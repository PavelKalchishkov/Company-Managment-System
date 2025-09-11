from django.db import models
from django.contrib.auth.models import AbstractUser
from common.validators import AllNumbersValidator, TenCharactersValidator

class CustomUser(AbstractUser):
    username = models.CharField(max_length=10,
                                unique=True,
                                )

    phone_number = models.CharField(max_length=100,
                                    validators=[AllNumbersValidator(),
                                                TenCharactersValidator()])

    email = models.EmailField(unique=True,max_length=30)