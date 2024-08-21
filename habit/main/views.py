from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib.auth import authenticate,login, logout 
from django.contrib import messages 
from .forms import SignUpForm,AddRecordForm, HabitCompletionForm
from .models import Habit, HabitCompletion
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from datetime import date


# Create your views here.

def home(request):
  
  #Check to see if logging in 
  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')
    #Authenticate
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request,user)
      messages.success(request, 'You have been logged in')
      return redirect('login')
    else:
      messages.success(request,"There was an error logging in, please try again")
      return redirect('login')
  else:
   return render(request, 'home.html', {})

  
def login_user(request):
  
  #Check to see if logging in 
  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')
    #Authenticate
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request,user)
        messages.success(request, 'You have been logged in')
        return redirect('myhabit')
    else: 
      messages.success(request,"There was an error logging in, please try again")
      return redirect('login_user')
  else:
   return render(request,'login_users.html',{})

   

def logout_user(request):
  logout(request)
  messages.success(request, 'You have been logged out ')
  return redirect('home')

def register_user(request):
  
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      #user authentication
      username = form.cleaned_data['username']
      password = form.cleaned_data['password1']
      user = authenticate(username=username,password=password)
      login(request,user)
      messages.success(request,'You have successfully registered, welcome')
      return redirect('login')
  else:
    form=SignUpForm() 
    return render(request, 'register.html', {'form':form})
  return render(request, 'register.html', {'form':form})

def habit_record(request,pk):
  if request.user.is_authenticated:
    #look up records
    habit_record = Habit.objects.get(id=pk)
    return render(request, 'record.html', {'habit_record':habit_record})
  else:
    messages.success(request,'You must be logged in to view the page')
    return redirect('home')

def delete_habit(request,pk):
  if request.user.is_authenticated:
    delete_records = Habit.objects.get(id=pk)
    delete_records.delete()
    messages.success(request,'Habit deleted successfully!')
    return redirect('myhabit')
  else:
    messages.success(request,'You must login to delete the habit!')
    return redirect('myhabit')

def add_habit(request):
    if request.method == 'POST':
        form = AddRecordForm(request.POST)
        if form.is_valid():
            # Save the form with the selected habit type
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            messages.success(request, 'Habit added successfully!')
            return redirect('myhabit')
        else:
            messages.error(request, 'Error adding habit. Please check the form.')
    else:
        form = AddRecordForm()
    
    return render(request, 'add_record.html', {'form': form})

      
def update_habit(request,pk):
  if request.user.is_authenticated:
    current_habit = get_object_or_404(Habit, pk=pk)

    if request.method=='POST':
      form = AddRecordForm(request.POST or None, instance=current_habit)
      if form.is_valid():
        form.save()
        messages.success(request, 'Habit has been updated')
        return redirect('myhabit')
    else:  
      form = AddRecordForm( instance=current_habit)
    return render(request, 'update_record.html',{'form':form})  
  else:
    messages.success(request, 'You must be logged in to add a habit')
    return redirect('home')
  
  
def about(request):
    return render(request, 'about.html')
  
def myhabit(request):
  # Filter habits for the logged-in user
    habits = Habit.objects.filter(user=request.user)
    return render(request, 'myhabit.html', {'habits':habits})

def mark_habit_completed(request, habit_id):
    try:
        habit = get_object_or_404(Habit, id=habit_id, user=request.user)
        today = date.today()
        completion, created = HabitCompletion.objects.get_or_create(habit=habit, date=today)
        if not completion.completed:
            completion.completed = True
            completion.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': True, 'message': 'Habit already marked as completed'})
    except Habit.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Habit not found'})

def track_progress(request, habit_id):
    habit = Habit.objects.get(id=habit_id, user=request.user)
    completions = HabitCompletion.objects.filter(habit=habit).order_by('date')
    return render(request, 'progress.html', {'habit': habit, 'completions': completions})

# other view functions
