# Generated by Django 2.0.2 on 2018-05-24 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnitBasicInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('businessName', models.CharField(max_length=100)),
                ('contactName', models.CharField(max_length=50)),
                ('serialNumber', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('location_add1', models.CharField(max_length=200)),
                ('location_add2', models.CharField(max_length=200)),
                ('location_city', models.CharField(max_length=20)),
                ('location_state', models.CharField(max_length=30)),
                ('location_zip', models.IntegerField()),
                ('issue', models.TextField()),
                ('warranty', models.BooleanField()),
                ('tsq', models.TextField()),
                ('techName', models.CharField(max_length=50)),
                ('techPhone', models.IntegerField()),
                ('techEmail', models.EmailField(max_length=254)),
                ('scheDate', models.DateField()),
            ],
        ),
    ]
