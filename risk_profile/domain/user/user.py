from django.db import models


class User(models.Model):
    age = models.CharField(max_length=50)
    dependents = models.CharField(max_length=9)
    house = models.Choices()
    income = models.IntegerField(max_length=50)
    marital_status = models.CharField(max_length=50)
    risk_questions = models.Choices()
    vehicle = models.CharField(max_length=50)

    def __str__(self):
        return self.name
