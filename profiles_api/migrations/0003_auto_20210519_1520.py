# Generated by Django 3.1 on 2021-05-19 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0002_profilefeeditem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profilefeeditem',
            old_name='ms_user_profile',
            new_name='user_profile',
        ),
    ]
