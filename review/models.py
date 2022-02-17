from django.core.validators import MaxValueValidator
from django.db import models

class TimestampedModel(models.Model):
  created_at = models.DataTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    abstract = True

class Review(TimestampedModel):
  conent = models.TextField()
  score = models.PositiveSmallIntegerField(
    validators=[
      MaxValueValidator(5),
    ]
  )