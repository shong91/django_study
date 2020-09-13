from django.db import models


# 모델이 바뀌면 항상 migration을 해줘야 한다!
# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)

    # default 를 지정하여 기존에 password 가 없던 데이터들은 null으로 set된다. (null=True 를 설정하지 않을 경우, 기본적으로 NOT NULL임 )
    password = models.CharField(max_length=20, default=None, null=True)
    image = models.CharField(max_length=500, default=None, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Review(models.Model):
    point = models.IntegerField()
    comment = models.CharField(max_length=500)

    # Many to One Relation: Foreign key 설정
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
