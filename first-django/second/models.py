from django.db import models


# Create your models here.
class Post(models.Model):
    # attributes 선언
    title = models.CharField(max_length=30)
    content = models.TextField() # 긴 문자열 - 길이 따로 선언하지 않음

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # num_stars = models.IntegerField() 숫자필드 선언
