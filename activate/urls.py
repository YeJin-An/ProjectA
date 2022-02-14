from django.urls import path, include
from rest_framework import routers
from activate.views import ActivateViewSet

router = routers.DefaultRouter()
router.register('activates',ActivateViewSet)

urlpatterns = [
  path('api/',include(router.urls)),
]