# Generated by Django 2.0.2 on 2018-05-24 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0003_auto_20180524_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unitbasicinfo',
            name='scheDate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='unitbasicinfo',
            name='techEmail',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='unitbasicinfo',
            name='techName',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='unitbasicinfo',
            name='techPhone',
            field=models.IntegerField(null=True),
        ),
    ]
