from django.urls import path
from . import views

urlpatterns = [
    path('computers/', views.Computer_List_View, name="computer_list"),
]
