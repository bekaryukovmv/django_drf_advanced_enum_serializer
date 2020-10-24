from rest_framework import permissions, viewsets

from first_app.models import Profile
from first_app.serializers import ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = Profile.objects.all()


# class SupplierTypesView(APIView):
#     serializer_class = LangSerializer
#     queryset = SupplierType.choices()
#     limit = 20
#     offset = 0

#     def get(self, request):
#         if request.query_params.get("offset") is not None:
#             try:
#                 self.offset = int(request.query_params.get("offset"))
#             except ValueError:
#                 return HttpResponseBadRequest("Can't parse offset")

#         if request.query_params.get("limit") is not None:
#             try:
#                 self.limit = int(request.query_params.get("limit"))
#             except ValueError:
#                 return HttpResponseBadRequest("Can't parse limit")

#         if request.query_params.get("search", None):
#             search = request.query_params.get("search")
#             if request.query_params.get("exclude", None):
#                 exclude = request.query_params.get("exclude").split(",")
#                 matching = [
#                     tz for tz in SupplierType.choices() if search.lower() in tz["named"] and tz["value"] not in exclude
#                 ]
#             else:
#                 matching = [tz for tz in SupplierType.choices() if search.lower() in tz["named"]]

#             matching = matching[self.offset :]
#             matching = matching[: self.limit]
#             return Response(matching, status=status.HTTP_200_OK)
#         if request.query_params.get("exclude", None):
#             exclude = request.query_params.get("exclude").split(",")

#             exclude_currencies = [tz for tz in SupplierType.choices() if tz["value"] not in exclude]
#             exclude_currencies = exclude_currencies[self.offset :]
#             exclude_currencies = exclude_currencies[: self.limit]
#             return Response(exclude_currencies, status=status.HTTP_200_OK)
#         try:
#             serializer = self.serializer_class(self.queryset, many=True)
#             result = list(serializer.data)
#             result = result[self.offset :]
#             result = result[: self.limit]
#             return Response(result, status=status.HTTP_200_OK)
#         except ObjectDoesNotExist:
#             return Response(status=404, data={"status": "ObjectDoesNotExist"})
