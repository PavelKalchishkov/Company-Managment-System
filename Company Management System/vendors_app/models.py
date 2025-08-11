from django.db import models
from common.validators import AllNumbersValidator, TenCharactersValidator


class Vendor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    phone_number = models.CharField(max_length=100,
                                    validators=[AllNumbersValidator,
                                                TenCharactersValidator])
    personal_phone_number = models.CharField(max_length=100,
                                             validators=[AllNumbersValidator,
                                                         TenCharactersValidator],
                                             null=True, blank=True)

    email = models.CharField(max_length=100)

    job_title = models.CharField(max_length=100)

    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    province = models.CharField(max_length=100, blank=True, null=True)
    ZIP = models.CharField(max_length=100, blank=True, null=True)

    fax_number = models.CharField(max_length=100, blank=True, null=True)
    web_page = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
