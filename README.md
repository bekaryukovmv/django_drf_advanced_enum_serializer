# django drf advanced edenum serializer

Some time ago, I ran into the problem of serializing a ChoiceField in Django Restframework.
I needed the field to be able to correctly accept and process both: the value and the display_name for the ChoiceField, of POST and PUT requests:

        {
        ...,
        "gender": value,
        ...
        }
        
        OR
        
        {
        ...,
        "gender": display_name,
        ...
        }

as well as the enums in the case. And also return the ChoiceField field as an object on GET:

        {"value": value, "display_name": display_name}

I had to little redefine the behavior a serializers.ChoiceField and create my own DisplayChoiceFieldSerializer. Now Django serializers work as I need :)

## Quick start

0.  Download django-advanced-enum-drf-0.1.tar.gz from this repo and install it with pip
        
        pip install --user <path>/django-advanced-enum-drf-0.1.tar.gz

1.  Add "advanced_enum_drf" to your INSTALLED_APPS setting like this:

        INSTALLED_APPS = [
            'advanced_enum_drf',
        ]

2.  Create your model included models.ChoiceField, and used classic Choice typle
    or models.TextChoices added in Django 3.
    Or you can also use your custom Enum class.
    If you use enum, inherit it to ChoicedEnum class like this:

        from django.db import models
        from django.utils.translation import gettext*lazy as *
        from advanced_enum_drf import ChoicedEnum

        class LoyalityPrograms(ChoicedEnum):
            PLATINUM_CARD = "Platinum"
            GOLDEN_CARD = "Gold"
            SILVER_CARD = "Silver"

        class Profile(models.Model):
            # old Django style
            GENDERS = [("M", "Male"), ("F", "Female"), ("U", "Undefined")]
            class YearInSchool(models.TextChoices):
                # New Django Style
                FRESHMAN = "FR", _("Freshman")
                SOPHOMORE = "SO", _("Sophomore")
                JUNIOR = "JR", _("Junior")
                SENIOR = "SR", _("Senior")
                GRADUATE = "GR", _("Graduate")

            gender = models.CharField(max_length=1, choices=GENDERS, default="U")
            loyality = models.CharField(max_length=8, choices=LoyalityPrograms.choices(),
            default=LoyalityPrograms.SILVER_CARD) # Enum style
            year_in_school = models.CharField(
                max_length=2,
                choices=YearInSchool.choices,
                default=YearInSchool.FRESHMAN,
            )

    ChoicedEnum have two advanced methods: choices and get_list_of_choices, for best serializers and models behavior.

3.  Create serializer used DisplayChoiceFieldSerializer, for field contained choices,
    like this:

        from advanced_enum_drf import DisplayChoiceFieldSerializer

        class ProfileSerializer(serializers.MyModelSerializer):
            gender = DisplayChoiceFieldSerializer(choices=Profile.GENDERS, required=False)
            loyality = DisplayChoiceFieldSerializer(choices=LoyalityPrograms.choices(), required=False)
            year_in_school = DisplayChoiceFieldSerializer(choices=Profile.YearInSchool, required=False)

            class Meta:
                model = Profile
                fields = "__all__"

4.  If you need a create api returned list of choices, you can do it one of this way:

        from advanced_enum_drf import ChoicesListView
        from .models import LoyalityPrograms, Profile

        class LoyalityChoicesListView(ChoicesListView):
            queryset = LoyalityPrograms.get_list_of_choices()

        class GenderChoicesListView(ChoicesListView):
            queryset = Profile.GENDERS

        class YearsToSchoolView(ChoicesListView):
            queryset = Profile.YearInSchool

    This class supported search and ordering query params, like original drf.

Best Regards!
