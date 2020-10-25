from django.urls import path
from rest_framework.routers import SimpleRouter

from first_app.views import GenderChoicesListView, LoyalityChoicesListView, ProfileViewSet, YearsToSchoolView

router = SimpleRouter()

router.register("profile", ProfileViewSet)

urlpatterns = router.urls

urlpatterns += [
    path("loyal-list/", LoyalityChoicesListView.as_view(), name="loyal list"),
    path("genders-list/", GenderChoicesListView.as_view(), name="genders list"),
    path("schoolyears-list/", YearsToSchoolView.as_view(), name="schoolyears list"),
]
