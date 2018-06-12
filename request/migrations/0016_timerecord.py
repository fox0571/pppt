# Generated by Django 2.0.6 on 2018-06-11 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0015_auto_20180610_0234'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.IntegerField()),
                ('call', models.DateTimeField()),
                ('pre_diagnosis', models.DateTimeField()),
                ('tech', models.DateTimeField()),
                ('part', models.DateTimeField()),
            ],
        ),
    ]
