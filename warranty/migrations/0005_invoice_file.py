# Generated by Django 2.0.6 on 2018-07-02 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warranty', '0004_invoice_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='file',
            field=models.FileField(null=True, upload_to='pppt/static/invoice/'),
        ),
    ]