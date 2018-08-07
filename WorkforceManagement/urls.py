from django.urls import path
from . import views
from .views import Employee_View


urlpatterns = [
    path('/computers/', views.Computer_List_View, name="computer_list"),
    path('/employees/', views.Employee_View.Employee_List_View.as_view(), name='Employee_List')
]
