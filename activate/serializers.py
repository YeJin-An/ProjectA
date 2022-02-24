from django.contrib.auth import get_user_model
from rest_framework import serializers
from activate.models import Activate


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username", "first_name", "last_name"]


class ActivateSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Activate
        fields = ["id","author","title","category","content","photo"]
