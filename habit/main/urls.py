from django.urls import path  
from . import views

urlpatterns = [
  path("", views.home, name="home"), 
  path("login/", views.login_user, name="login"),  
  path("logout/", views.logout_user, name="logout"),  
  path("register/", views.register_user, name="register"), 
  path("habit/<int:pk>", views.habit_record, name="habit"), 
  path("delete_habit/<int:pk>", views.delete_habit, name="delete_habit"), 
  path("add_habit/", views.add_habit, name="add_habit"), 
  path("update_habit/<int:pk>", views.update_habit, name="update_habit"), 
  path("about/", views.about, name="about"), 
  path("myhabit/", views.myhabit, name="myhabit"), 
  path("mark_habit_completed/<int:habit_id>/",views.mark_habit_completed, name="mark_habit_completed"),
  
  path(" track_progress/<int:pk>", views. track_progress, name=" track_progress"), 

]