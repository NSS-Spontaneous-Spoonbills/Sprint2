from django.urls import path
from . import views
from WorkforceManagement.views import Employee_View


urlpatterns = [
    path('/computers/', views.Computer_List_View, name="computer_list"),
    path('/employees/', views.Employee_View.Employee_List_View.as_view(), name='employee_list'),
    path('/employees/<int:pk>', views.Employee_View.Employee_Detail_View.as_view(), name='employee_detail'),
    path('/computers/<int:pk>/', views.Computer_Detail_View, name="computer_detail"),
    path('/training_progs/', views.Training_List_View, name="training_prog_list"),
    path('/departments/', views.Department_List_View, name="department_list"),
]
