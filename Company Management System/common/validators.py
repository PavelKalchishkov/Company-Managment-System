from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
import re


@deconstructible
class AllNumbersValidator:
    def __call__(self, value: str, *args, **kwargs):
        if not re.fullmatch(r'[0-9]+', value):
            raise ValidationError("Incorrect phone number!")


@deconstructible
class TenCharactersValidator:
    def __call__(self, value: str, *args, **kwargs):
        if len(value) != 10:
            raise ValidationError("Your phone number must be 10 digits!")

@deconstructible
class PositiveFloatValidator:
    def __call__(self, value: str, *args, **kwargs):
        if float(value) < 0:
            raise ValidationError("Value must be positive!")