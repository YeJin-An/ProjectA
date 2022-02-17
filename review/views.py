from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from rest_framework import viewsets

from review.forms import ReviewForm
from review.models import Review
from review.serializers import ReviewSerializer

review_list = ListView.as_view(model=Review)

review_new = CreateView.as_view(
  model=Review,
  form_class=ReviewForm,
  success_url=reverse_lazy("review:review_list"),
)

class ReviewViewSet(viewsets.ModelViewSet):
  queryset = Review.objects.all()
  serializer_class = ReviewSerializer