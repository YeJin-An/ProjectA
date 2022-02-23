from django.conf import settings
from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models

class Activate(models.Model):

    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, db_index=True,
                             validators=[
                                 MinLengthValidator(3),
                                 RegexValidator(r"[ㄱ-힣]", message="한글을 입력해주세요."),
                             ])
    
    category = models.CharField(
        max_length=1,
        choices=[
            ("1", "대중교통 이용"),
            ("2", "장바구니 사용"),
            ("3", "스마트 영수증"),
            ("4", "텀블러 사용"),
            ("5", "올바른 분리배출"),
        ]
    )
    content = models.TextField()
    photo = models.ImageField(blank=True)