from django.urls import path, include
from rest_framework import routers
from notice.views import NoticeViewSet

router = routers.DefaultRouter()
router.register('notices', NoticeViewSet)

urlpatterns = [
  path('',include(router.urls))
]