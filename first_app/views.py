from rest_framework import permissions, viewsets

from first_app.models import Profile
from first_app.serializers import ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = Profile.objects.all()
