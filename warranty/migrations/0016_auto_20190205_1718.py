# Generated by Django 2.0.6 on 2019-02-05 23:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('warranty', '0015_auto_20181102_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='approved_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='approver', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='invoice',
            name='dispute_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='invoice_type',
            field=models.IntegerField(choices=[(0, 'from service company'), (1, 'from inhouse tech')], default=0),
        ),
    ]
