# Generated by Django 2.0.6 on 2018-10-11 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0047_auto_20180929_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partrequest',
            name='sn',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
    ]
