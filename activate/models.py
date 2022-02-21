from django.conf import settings
from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models
from user.models import User

class Activate(models.Model):
  id = models.CharField(max_length=20)
  category = models.IntegerField()
  title = models.CharField(max_length=100,  db_index=True,
                             validators=[
                                 MinLengthValidator(3),
                                 RegexValidator(r"[ㄱ-힣]", message="한글을 입력해주세요."),
                             ])
  content = models.TextField()
  photo = models.TextField()
  user = models.OneToOneField(User,primary_key=True, on_delete=models.CASCADE)