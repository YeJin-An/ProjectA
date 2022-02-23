from django.conf import settings
from django.db import models
from user.models import User

class Notice(models.Model):

  id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=100)
  content = models.TextField()
  created_at = models.DateField()
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)