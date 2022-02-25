from django.contrib.auth import get_user_model
from rest_framework import serializers
from notice.models import Notice

class AuthorSerializer(serializers.ModelSerializer):
  class Meta:
    model = get_user_model()
    fields = ["username","first_name",'last_name']

class NoticeSerializer(serializers.ModelSerializer):
  author = AuthorSerializer(read_only=True)
  
  class Meta:
    model = Notice
    fields = ["id","author","title","content","created_at"]
#fields = "__all__"