class ListChoiceFilteredMixin:
    def get_excluded_items(self):
        excluded_items = []
        if self.request.query_params.get("exclude"):
            excluded_items = [x.strip().lower() for x in self.request.query_params["exclude"].split(", ")]

        return excluded_items

    def search_filter_query(self, queryset):
        filtered_queryset = []
        if self.request.query_params.get("search"):
            search_params = [x.strip() for x in self.request.query_params["search"].split()]

            for i in queryset:
                for j in search_params:
                    excluded_items = self.get_excluded_items()

                    if (j.lower() in i["value"].lower() or j.lower() in i["display_name"].lower()) and (
                        i["display_name"].lower() not in excluded_items and i["value"].lower() not in excluded_items
                    ):
                        filtered_queryset.append(i)

            queryset = filtered_queryset
        return queryset

    def get_ordering_params(self):
        ordering_params = [
            x.strip().lower()
            for x in self.request.query_params["ordering"].split(", ")
            if x.lower() in ["value", "-value", "display_name", "-display_name"]
        ]

        assert len(ordering_params) <= 2, "Too many ordering params"

        return ordering_params

    def get_flag_and_ordered_func(self, ordering_params):
        flag = ordering_params[0].startswith("-")

        if len(ordering_params) == 2:
            ordered_func = lambda i: (i[ordering_params[0].strip("-")], i[ordering_params[1].strip("-")])
        else:
            ordered_func = lambda i: (i[ordering_params[0].strip("-")])

        return flag, ordered_func

    def search_order_query(self, queryset):
        if self.request.query_params.get("ordering"):
            flag, ordered_func = self.get_flag_and_ordered_func(self.get_ordering_params())
            queryset = sorted(queryset, key=ordered_func, reverse=flag)

        return queryset
