# Generated by Django 3.1 on 2021-05-19 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0003_auto_20210519_1520'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profilefeeditem',
            old_name='create_on',
            new_name='created_on',
        ),
    ]