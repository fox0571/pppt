# Generated by Django 2.0.6 on 2018-12-06 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0052_auto_20181106_1122'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='partrequest',
            options={'ordering': ('number',), 'permissions': (('change_part_status', 'Can change the status of part request'),)},
        ),
    ]