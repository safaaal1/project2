# Generated by Django 3.1.13 on 2022-01-05 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20220105_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='about',
            field=models.TextField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='rules',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
