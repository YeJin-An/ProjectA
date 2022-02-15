from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer as OrigTokenObtainPairSerializer,
    TokenRefreshSerializer as OrigTokenRefreshSerializer,
)


User = get_user_model()


class UserCreationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ["username", "password"]


    def create(self, validated_data):
        # 리턴 : 생성된 User 모델 인스턴스
        username = validated_data["username"]
        password = validated_data["password"]

        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()

        return new_user


class TokenObtainPairSerializer(OrigTokenObtainPairSerializer):

    # access/refresh 속성 외에 추가 속성
    def validate(self, attrs):
        data = super().validate(attrs)
        data["username"] = self.user.username
        # TODO: 프로필 이미지 URL
        return data


class TokenRefreshSerializer(OrigTokenRefreshSerializer):
    pass
