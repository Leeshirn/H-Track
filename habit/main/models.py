from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#habits users want to track
class Habit(models.Model):
    
    HABIT_FREQUENCY_CHOICES = (
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('custom','Custom'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1) 
    
    name = models.CharField(max_length=100)
    
    category = models.TextField(default= "")
    
    description = models.TextField()
    
    frequency = models.CharField(max_length=20, choices=HABIT_FREQUENCY_CHOICES)
    
    start_date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
      return (f"{self.name}-{self.category}-{self.description}-{self.frequency}-{self.start_date}-{self.user}")
  
class HabitCompletion(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    date = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.habit.name} - {self.date}-{self.completed}"