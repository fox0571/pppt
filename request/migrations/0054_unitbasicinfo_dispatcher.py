# Generated by Django 2.0.6 on 2018-12-15 17:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('request', '0053_auto_20181206_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='unitbasicinfo',
            name='dispatcher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
