# Generated by Django 3.1 on 2021-05-19 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0004_auto_20210519_1524'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profilefeeditem',
            old_name='user_profile',
            new_name='ms_user_profile',
        ),
    ]
