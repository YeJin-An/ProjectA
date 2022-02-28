from django.contrib.auth import get_user_model
from rest_framework import serializers
from notice.models import Notice

class AuthorSerializer(serializers.ModelSerializer):
  class Meta:
    model = get_user_model()
    fields = ["username","first_name",'last_name']

class NoticeSerializer(serializers.ModelSerializer):
  author = AuthorSerializer()
  
  class Meta:
    model = Notice
    fields = ["id",'author',"title","content","created_at",'author']
    # fields = "__all__"


# 비로그인 사용자용
# class BoticeAnanymousSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = Notice
#     fields = ["id", "title","content"]