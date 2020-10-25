from enum import Enum


class ChoicedEnum(Enum):
    @classmethod
    def choices(cls):
        return [(i.value, str(i.name).replace("_", " ").title()) for i in cls]

    @classmethod
    def get_list_of_choices(cls):
        return [{"value": i.value, "display_name": str(i.name).replace("_", " ").title()} for i in cls]


class LoyalityPrograms(ChoicedEnum):
    PLATINUM_CARD = "Platinum"
    GOLDEN_CARD = "Gold"
    SILVER_CARD = "Silver"
