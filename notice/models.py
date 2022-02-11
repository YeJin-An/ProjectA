from django.conf import settings
from django.db import models
from user.models import User

class Notice(models.Model):
  id = models.CharField(max_length=15)
  title = models.CharField(max_length=100)
  content = models.TextField()
  created_at = models.DateField()
  user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)