from django.urls import path
from rest_framework.routers import SimpleRouter

from first_app.views import GenderChoicesListView, LoyalityChoicesListView, ProfileViewSet

router = SimpleRouter()

router.register("profile", ProfileViewSet)

urlpatterns = router.urls

urlpatterns += [
    path("loyal-list/", LoyalityChoicesListView.as_view(), name="choiced list"),
    path("genders-list/", GenderChoicesListView.as_view(), name="choiced list"),
]
