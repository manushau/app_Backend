# Generated by Django 4.2.11 on 2024-05-02 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend_server', '0026_alter_workoutentry_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workoutentry',
            name='workout_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend_server.workouttype'),
        ),
    ]
