# Generated by Django 2.0.3 on 2018-05-28 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20180527_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='group',
            field=models.CharField(choices=[('dispatcher', 'DISPATCHER'), ('operator', 'OPERATOR'), ('warranty', 'WARRANTY'), ('admin', 'ADMIN')], default='operator', max_length=15),
        ),
    ]
