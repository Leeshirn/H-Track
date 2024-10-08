# Generated by Django 5.0.2 on 2024-08-21 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_remove_habit_frequency'),
    ]

    operations = [
        migrations.AddField(
            model_name='habitcompletion',
            name='count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterUniqueTogether(
            name='habitcompletion',
            unique_together={('habit', 'date')},
        ),
    ]
