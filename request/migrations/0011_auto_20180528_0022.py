# Generated by Django 2.0.3 on 2018-05-28 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0010_unitbasicinfo_finished'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unitbasicinfo',
            old_name='reciever',
            new_name='receiver',
        ),
    ]
