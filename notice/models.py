from re import A
from django.conf import settings
from django.db import models
from user.models import User
from django.core.exceptions import ValidationError


def validate_even(value):
    if value < '5':
      raise ValidationError(
          _('%(value)s is not an even number'),
            params={'value': value},
      )

class Notice(models.Model):
  id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=5, validators=[validate_even])
  content = models.TextField()
  created_at = models.DateField()
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

