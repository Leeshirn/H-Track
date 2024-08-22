from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 
from django import forms 
from .models import Habit

class SignUpForm(UserCreationForm):
  
   class Meta:
      model = User
      fields = ('username', 'password1', 'password2')
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

  
  class Meta:
      model = Habit
      fields = ('name', 'category','description')

'''class HabitCompletionForm(forms.ModelForm):
    class Meta:
        model = HabitCompletion
        fields = ['date', 'completed']'''