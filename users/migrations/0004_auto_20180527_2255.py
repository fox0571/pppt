# Generated by Django 2.0.3 on 2018-05-27 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_users_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='tasks',
        ),
        migrations.AddField(
            model_name='users',
            name='current_month',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='users',
            name='current_tasks',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='users',
            name='total_tasks',
            field=models.IntegerField(default=0),
        ),
    ]
