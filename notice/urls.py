from django.urls import path, include
from rest_framework import routers
from notice.views import NoticeViewSet

app_name = 'notice'

router = routers.DefaultRouter()
router.register('notices', NoticeViewSet)

urlpatterns = [
  path('api/',include(router.urls)),
]