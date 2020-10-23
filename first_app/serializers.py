from rest_framework import serializers

from first_app.models import LoyalityPrograms, Profile


class DisplayChoiceSerializer(serializers.ChoiceField):
    def __init__(self, *args, **kwargs):
        super(DisplayChoiceSerializer, self).__init__(*args, **kwargs)
        self.choice_strings_to_values = {str(key): str(value) for key, value in self.choices.items()}
        self.choice_strings_to_keys = {str(value): str(key) for key, value in self.choices.items()}

    def to_internal_value(self, data):
        if data == "" and self.allow_blank:
            return ""

        try:
            return self.choice_strings_to_keys[str(data)]
        except KeyError:
            if self.choice_strings_to_values.get(str(data)):
                return str(data)
            self.fail("invalid_choice", input=data)

    def to_representation(self, value):
        if value in ("", None):
            return value
        return {"value": value, "display_name": self.choice_strings_to_values.get(str(value), value)}


class ProfileSerializer(serializers.ModelSerializer):
    gender = DisplayChoiceSerializer(choices=Profile.GENDERS)
    loyality = DisplayChoiceSerializer(choices=LoyalityPrograms.choices())

    class Meta:
        model = Profile
        fields = "__all__"
