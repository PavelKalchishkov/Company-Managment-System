from django.db import models
from common.validators import AllNumbersValidator, TenCharactersValidator



class Vendor(models.Model):
    name = models.CharField(max_length=100,
                            default="new_vendor")

    phone_number = models.CharField(max_length=100,
                                    validators=[AllNumbersValidator,
                                                TenCharactersValidator])

    additional_information = models.TextField(max_length=500,
                                              default='')
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
