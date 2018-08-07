from django.urls import path
from . import views

urlpatterns = [
    path('/computers/', views.Computer_List_View, name="computer_list"),
    path('/training_progs/', views.Training_List_View, name="training_prog_list"),
]
