from enum import Enum

from rest_framework import serializers

from first_app.models import LoyalityPrograms, Profile


class DisplayChoiceFieldSerializer(serializers.ChoiceField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, value in self.choices.items():
            if isinstance(key, Enum):
                self.choice_strings_to_values = {str(key).lower(): key for key in self.choices}
                self.choice_strings_to_keys = {str(key.label).lower(): str(key) for key in self.choices}
                self.choice_strings_to_representation = {str(key): str(key.label) for key in self.choices}
            else:
                self.choice_strings_to_values = {str(key).lower(): key for key in self.choices}
                self.choice_strings_to_keys = {str(value).lower(): str(key) for key, value in self.choices.items()}
                self.choice_strings_to_representation = {str(key): str(value) for key, value in self.choices.items()}
            break

    def to_internal_value(self, data):
        if data == "" and self.allow_blank:
            return ""

        try:
            return self.choice_strings_to_keys[str(data).lower()]
        except KeyError:
            if self.choice_strings_to_values.get(str(data).lower()):
                return self.choice_strings_to_values.get(str(data).lower())
            self.fail("invalid_choice", input=data)

    def to_representation(self, value):
        if value in ("", None):
            return value
        return {"value": value, "display_name": self.choice_strings_to_representation.get(str(value), value)}


class ProfileSerializer(serializers.ModelSerializer):
    gender = DisplayChoiceFieldSerializer(choices=Profile.GENDERS, required=False)
    loyality = DisplayChoiceFieldSerializer(choices=LoyalityPrograms.choices(), required=False)
    year_in_school = DisplayChoiceFieldSerializer(choices=Profile.YearInSchool, required=False)

    class Meta:
        model = Profile
        fields = "__all__"


class ChoicedListSerializer(serializers.Serializer):
    value = serializers.CharField()
    display_name = serializers.CharField()
