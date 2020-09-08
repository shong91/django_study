# Generated by Django 3.1.1 on 2020-09-08 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

# >>> Restaurant.objects.filter(name='Deli Shsop').values()
# <QuerySet []>
# >>> Restaurant.objects.exclude(name='Deli Shop').values()
# >>> Restaurant.objects.order_by('-created_at')   (-):역순정렬
# QuerySet 은 아직 데이터가 호출되지 않은 상태. [i], .name 등을 사용하여야 데이터가 호출된다.

# Column Lookup 으로 조건 검색하기
# field lookup : (속성)__(조건)
# ex) name__exact, name__contains
# created_at__lte, created_at__gte (less than / equal, greater than / equal)
# startswith, endswith, in=[], range=()

