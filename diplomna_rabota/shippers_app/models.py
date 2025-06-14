from django.db import models

class Shipper(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11)
    salary = models.IntegerField()
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
