# Generated by Django 3.1.1 on 2020-09-13 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('third', '0002_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='image',
            field=models.CharField(default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='password',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
    ]
