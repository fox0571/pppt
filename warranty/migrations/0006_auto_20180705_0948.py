# Generated by Django 2.0.6 on 2018-07-05 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warranty', '0005_invoice_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='invoice/'),
        ),
    ]