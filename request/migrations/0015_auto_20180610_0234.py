# Generated by Django 2.0.3 on 2018-06-10 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0014_partrequest_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unitbasicinfo',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='unitbasicinfo',
            name='techPhone',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
