from django.conf import settings
from django.db import models
from user.models import User

class Activate(models.Model):
  id = models.CharField(max_length=20)
  category = models.IntegerField()
  title = models.CharField(max_length=100)
  content = models.TextField()
  image = models.TextField()
  user = models.OneToOneField(User,primary_key=True, on_delete=models.CASCADE)