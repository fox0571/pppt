# Generated by Django 2.0.6 on 2018-07-13 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0039_auto_20180713_1203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filesimplemodel',
            name='sksid',
        ),
        migrations.AddField(
            model_name='filesimplemodel',
            name='incident',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='request.UnitBasicInfo'),
        ),
        migrations.AlterField(
            model_name='filesimplemodel',
            name='file_field',
            field=models.FileField(upload_to='%Y/%m/%d/'),
        ),
    ]
