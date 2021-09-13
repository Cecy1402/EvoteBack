from rest_framework import routers
from .views import UserViewSet

router = routers.SimpleRouter()
router.register('Users', UserViewSet)


urlpatterns = router.urls