# habits/management/commands/create_daily_records.py
from django.core.management.base import BaseCommand
from datetime import date
from habits.models import Habit, HabitCompletion

class Command(BaseCommand):
    help = 'Create daily records for each habit'

    def handle(self, *args, **kwargs):
        today = date.today()
        habits = Habit.objects.all()
        for habit in habits:
            HabitCompletion.objects.get_or_create(habit=habit, date=today)
        self.stdout.write(self.style.SUCCESS('Successfully created daily records'))
