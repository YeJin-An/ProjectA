from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ActivateSerializer
from .models import Activate

class ActivateViewSet(viewsets.ModelViewSet):
  queryset = Activate.objects.all()
  serializer_class = ActivateSerializer
  
