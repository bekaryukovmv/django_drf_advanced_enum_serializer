from django.db.models.enums import ChoicesMeta
from django.db.models.query import QuerySet
from rest_framework import permissions, viewsets
from rest_framework.generics import ListAPIView

from first_app.models import Profile
from first_app.serializers import ChoicedListSerializer, ProfileSerializer

from .choices import LoyalityPrograms
from .mixins import ListChoiceFilteredMixin


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = Profile.objects.all()


class ChoicesListView(ListChoiceFilteredMixin, ListAPIView):
    serializer_class = ChoicedListSerializer

    def filter_queryset(self, queryset):
        return self.search_order_query(self.search_filter_query(queryset))

    def get_queryset(self):
        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method." % self.__class__.__name__
        )

        queryset = self.queryset
        print(queryset)
        if isinstance(queryset, QuerySet):
            queryset = queryset.all()
        elif isinstance(queryset, ChoicesMeta):
            queryset = [{"value": key, "display_name": key.label} for key in queryset]
        elif isinstance(queryset[0], tuple):
            queryset = [{"value": key, "display_name": val} for (key, val) in queryset]
        # else:
        #     raise TypeError("Unknown type of queryset!")

        return queryset


class LoyalityChoicesListView(ChoicesListView):
    queryset = LoyalityPrograms.get_list_of_choices()


class GenderChoicesListView(ChoicesListView):
    queryset = Profile.GENDERS


class YearsToSchoolView(ChoicesListView):
    queryset = Profile.YearInSchool
