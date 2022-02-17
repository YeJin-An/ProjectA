from django.urls import path, include
from rest_framework import routers
from user.views import UserViewSet

app_name = 'user'

router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns= [
  path('api/',include(router.urls)),
]