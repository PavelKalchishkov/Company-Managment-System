from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11)
    age = models.IntegerField()
    brute_salary = models.IntegerField()

    def __str__(self):
        return self.name