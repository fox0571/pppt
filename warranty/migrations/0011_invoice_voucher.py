# Generated by Django 2.0.6 on 2018-08-01 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warranty', '0010_invoice_processed'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='voucher',
            field=models.CharField(default='------', max_length=15),
        ),
    ]