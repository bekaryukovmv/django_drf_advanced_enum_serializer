from enum import Enum

from django.db import models


class LoyalityPrograms(Enum):
    PLATINUM = "PLATINUM CARD"
    GOLD = "GOLDEN CARD"
    SILVER = "SILVER CARD"

    @classmethod
    def choices(cls):
        return [(key.name, key.value) for key in cls]


class Profile(models.Model):
    GENDERS = [("M", "Male"), ("F", "Female"), ("U", "Undefined")]

    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=GENDERS, default="U")
    age = models.IntegerField(default=0)
    loyality = models.CharField(max_length=8, choices=LoyalityPrograms.choices(), default=LoyalityPrograms.SILVER.name)
