from django.urls import path, include
from rest_framework import routers
from notice.views import Notice

app_name = 'notice'

router = routers.DefaultRouter()
router.register('notices', Notice)

urlpatterns = [
  path('api/',include(router.urls)),
]