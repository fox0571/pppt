# Generated by Django 2.0.2 on 2018-05-24 22:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0002_unitbasicinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='unitbasicinfo',
            name='callTime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='unitbasicinfo',
            name='warranty',
            field=models.NullBooleanField(),
        ),
    ]
