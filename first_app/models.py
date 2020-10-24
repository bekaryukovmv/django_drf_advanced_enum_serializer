from django.db import models

from .choices import LoyalityPrograms


class Profile(models.Model):
    GENDERS = [("M", "Male"), ("F", "Female"), ("U", "Undefined")]

    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=GENDERS, default="U")
    age = models.IntegerField(default=0)
    loyality = models.CharField(max_length=8, choices=LoyalityPrograms.choices(), default=LoyalityPrograms.SILVER.name)
