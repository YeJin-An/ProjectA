from django.urls import path, include
from rest_framework.routers import DefaultRouter
from activate import views 

app_name = 'activate'

router = DefaultRouter()
router.register('activates',views.ActivateViewSet)

urlpatterns = [
  path('api/',include(router.urls)),
]