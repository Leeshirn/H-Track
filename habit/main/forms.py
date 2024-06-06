from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 
from django import forms 
from .models import Habit,HabitCompletion

class SignUpForm(UserCreationForm):
  email = forms.EmailField(label="",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
  first_name = forms.CharField(label="", max_length="100", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
  last_name = forms.CharField(label="",max_length="100", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
  class Meta:
    model = User
    fields = ('username','first_name', 'last_name','email', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
      super(SignUpForm, self).__init__(*args, **kwargs)

      self.fields['username'].widget.attrs['class'] = 'form-control'
      self.fields['username'].widget.attrs['placeholder'] = 'Username'
      self.fields['username'].label = ''
      

      self.fields['password1'].widget.attrs['class'] = 'form-control'
      self.fields['password1'].widget.attrs['placeholder'] = 'Password'
      self.fields['password1'].label = ''
      self.fields['password1'].help_text = None

      self.fields['password2'].widget.attrs['class'] = 'form-control'
      self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
      self.fields['password2'].label = ''
      self.fields['password2'].help_text = None


#add habits form
class AddRecordForm(forms.ModelForm):
  name= forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Habit Name', "class":"form-control"}), label="")
  category= forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Category', "class":"form-control"}), label="")
  description= forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Description', "class":"form-control"}), label="")
  frequency= forms.ChoiceField(choices=Habit.HABIT_FREQUENCY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}),label = "Frequency")
  custom_days = forms.ModelMultipleChoiceField(
        queryset=Habit.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        label="Custom Days"
    )
  
  class Meta:
      model = Habit
      fields = ('name', 'category','description','frequency', 'custom_days')
      
      



class HabitCompletionForm(forms.ModelForm):
    class Meta:
        model = HabitCompletion
        fields = ['date', 'completed']