from django.db import models
from django.contrib.auth.models import AbstractUser
from common.validators import AllNumbersValidator, TenCharactersValidator
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    username = models.CharField(max_length=10,
                                unique=True,
                                verbose_name=_('Username'),
                                )

    phone_number = models.CharField(max_length=100,
                                    verbose_name=_('phone_number'),
                                    validators=[AllNumbersValidator(),
                                                TenCharactersValidator()])

    email = models.EmailField(unique=True,max_length=30, verbose_name=_('email'),)