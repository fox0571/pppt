# Generated by Django 2.0.6 on 2018-06-13 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0022_auto_20180612_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='unitbasicinfo',
            name='tech_add1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='unitbasicinfo',
            name='tech_add2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='unitbasicinfo',
            name='tech_city',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='unitbasicinfo',
            name='tech_state',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='unitbasicinfo',
            name='tech_zip',
            field=models.IntegerField(null=True),
        ),
    ]
