from django.db import models
from django.utils.translation import gettext_lazy as _

from .choices import LoyalityPrograms


class Profile(models.Model):
    GENDERS = [("M", "Male"), ("F", "Female"), ("U", "Undefined")]

    class YearInSchool(models.TextChoices):
        FRESHMAN = "FR", _("Freshman")
        SOPHOMORE = "SO", _("Sophomore")
        JUNIOR = "JR", _("Junior")
        SENIOR = "SR", _("Senior")
        GRADUATE = "GR", _("Graduate")

    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=GENDERS, default="U")
    age = models.IntegerField(default=0)
    loyality = models.CharField(max_length=8, choices=LoyalityPrograms.choices(), default=LoyalityPrograms.SILVER.name)
    year_in_school = models.CharField(
        max_length=2,
        choices=YearInSchool.choices,
        default=YearInSchool.FRESHMAN,
    )
