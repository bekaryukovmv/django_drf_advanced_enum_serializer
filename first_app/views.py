import operator
from collections import OrderedDict

from rest_framework import filters, pagination, permissions, viewsets
from rest_framework.generics import ListAPIView

from first_app.models import Profile
from first_app.serializers import ChoicedListSerializer, ProfileSerializer

from .choices import LoyalityPrograms


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = Profile.objects.all()


class ChoicesListView(ListAPIView):
    serializer_class = ChoicedListSerializer

    def filter_queryset(self, queryset):
        # FIXME add exclude field
        filtered_queryset = []
        if self.request.query_params.get("search"):
            search_params = [x.strip() for x in self.request.query_params["search"].split()]

            for i in queryset:
                for j in search_params:
                    if j.lower() in i["value"].lower() or j.lower() in i["display_name"].lower():
                        filtered_queryset.append(i)

            queryset = filtered_queryset

        if self.request.query_params.get("ordering"):
            ordering_params = [
                x.strip().lower()
                for x in self.request.query_params["ordering"].split(", ")
                if x.lower() in ["value", "-value", "display_name", "-display_name"]
            ]

            assert len(ordering_params) <= 2, "Too many ordering params"

            flag = False

            if len(ordering_params) == 2:
                ordered_func = lambda i: (i[ordering_params[0].strip("-")], i[ordering_params[1].strip("-")])

            if ordering_params[0].startswith("-"):
                flag = True

            ordered_func = lambda i: (i[ordering_params[0].strip("-")])

            queryset = sorted(queryset, key=ordered_func, reverse=flag)

        return queryset


class LoyalityChoicesListView(ChoicesListView):
    queryset = LoyalityPrograms.get_list_of_choices()
