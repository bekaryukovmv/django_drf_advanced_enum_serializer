from enum import Enum


class ChoicedEnum(Enum):
    @classmethod
    def choices(cls):
        return [(i.name, i.value) for i in cls]

    @classmethod
    def get_list_of_choices(cls):
        return [{"value": i.name, "display_name": i.value} for i in cls]


class LoyalityPrograms(ChoicedEnum):
    PLATINUM = "PLATINUM CARD"
    GOLD = "GOLDEN CARD"
    SILVER = "SILVER CARD"
