# Generated by Django 4.2.11 on 2024-04-24 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_server', '0013_rename_message_messages_message_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='timestamp_read',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='messages',
            name='timestamp_sent',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
