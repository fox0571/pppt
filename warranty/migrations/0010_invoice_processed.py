# Generated by Django 2.0.6 on 2018-07-19 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warranty', '0009_auto_20180713_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='processed',
            field=models.BooleanField(default=False),
        ),
    ]
