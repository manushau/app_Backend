# Generated by Django 4.2.11 on 2024-04-27 00:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend_server', '0020_rename_user_myuser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accountdetails',
            old_name='user_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='accountdetails',
            old_name='user_username',
            new_name='username',
        ),
    ]