from django.urls.conf import path
from rest_framework import routers
from .views import UserViewSet
router = routers.SimpleRouter()

router.register('users',UserViewSet)

urlpatterns = router.urls