from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView, FormView, DetailView, CreateView
from WorkforceManagement.models import Training_Prog

def Training_List_View(request):
    """ Displays all training programs in the company """
    training_progs = Training_Prog.objects.all()
    return render(request, 'WorkforceManagement/Training_list.html', {'training_progs': training_progs})