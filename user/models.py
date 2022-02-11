from django.db import models

class User(models.Model):
  id = models.CharField(max_length=10, primary_key=True)
  password = models.TextField()
  address = models.CharField(max_length=100,null=True)
  email=models.CharField(max_length=50)
  phonenumber=models.CharField(max_length=11)