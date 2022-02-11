from django.shortcuts import render
from rest_framework import viewsets
from .serializers import NoticeSerializer
from .models import Notice

class NoticeViewSet(viewsets.ModelViewSet):
  queryset = Notice.objects.all()
  serializer_class = NoticeSerializer
