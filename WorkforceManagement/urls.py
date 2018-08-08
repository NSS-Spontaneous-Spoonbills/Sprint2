from django.urls import path
from . import views
from .views import Employee_View


urlpatterns = [
    path('computers/', views.Computer_List_View, name="computer_list"),
    path('employees/', views.Employee_View.Employee_List_View.as_view(), name='Employee_List'),
    path('computers/<int:pk>/', views.Computer_Detail_View, name="computer_detail"),
    path('training_programs/', views.Training_List_View, name="training_list"),
    path('training_programs/<int:pk>/', views.Training_Detail_View, name="training_detail"),
    path('departments/', views.Department_List_View, name="department_list"),

]
