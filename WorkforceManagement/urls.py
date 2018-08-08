from django.urls import path
from . import views
from .views import Employee_View


urlpatterns = [
<<<<<<< HEAD
    path('/computers/', views.Computer_List_View, name="computer_list"),
    path('/computers/<int:pk>/', views.Computer_Detail_View, name="computer_detail"),
    path('/computers/<int:pk>/', views.Computer_Detail_View, name="computer_detail"),
    path('/training_programs/', views.Training_List_View, name="training_list"),
    path('/training_programs/<int:pk>/', views.Training_Detail_View, name="training_detail"),
    path('departments/', views.Department_List_View, name="department_list"),

=======
    path('computers/', views.Computer_List_View, name="computer_list"),
    path('employees/', views.Employee_View.Employee_List_View.as_view(), name='Employee_List'),
    path('computers/<int:pk>/', views.Computer_Detail_View, name="computer_detail"),
    path('training_progs/', views.Training_List_View, name="training_prog_list"),
    path('departments/', views.Department_List_View, name="department_list"),
>>>>>>> 63dc8f086bfe06cdb4211162685d349481aaf027
]
