# Generated by Django 5.0.2 on 2024-06-14 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_rename_created_at_habit_start_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habit',
            name='frequency',
        ),
    ]