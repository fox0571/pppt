# Generated by Django 2.0.2 on 2018-05-30 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0013_auto_20180530_1008'),
    ]

    operations = [
        migrations.AddField(
            model_name='partrequest',
            name='code',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
