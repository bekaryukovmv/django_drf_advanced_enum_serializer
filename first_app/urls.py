from rest_framework.routers import SimpleRouter

from first_app.views import ProfileViewSet

router = SimpleRouter()

router.register("profile", ProfileViewSet)

urlpatterns = router.urls
