from django.urls import path
from . import views
# from .views import Employee_View


urlpatterns = [
    path('computers/', views.Computer_List_View, name="computer_list"),
    path('computers/<int:pk>/', views.Computer_Detail_View, name="computer_detail"),
    path('computers/new', views.Computer_New_View, name='computer_new'),
    path('computers/<int:pk>/update/',
         views.Computer_Update_View, name='computer_update'),
    path('employees/', views.Employee_View.Employee_List_View.as_view(),
         name='Employee_List'),
    path('training_progs/', views.Training_List_View, name="training_prog_list"),
    path('departments/', views.Department_List_View, name="department_list"),
]
