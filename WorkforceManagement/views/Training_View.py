from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView, FormView, DetailView, CreateView
from WorkforceManagement.forms import *


from WorkforceManagement.models import Training_Prog

def Training_List_View(request):
    """ Displays all training programs in the company """
    training_progs = Training_Prog.objects.all()
    return render(request, 'WorkforceManagement/Training_List.html', {'training_progs': training_progs})


def Training_Detail_View(request, pk):
    """Displays details about a specific program"""
    prog = get_object_or_404(Training_Prog, pk=pk)
    return render(request, 'WorkforceManagement/Training_Detail.html', {'prog': prog})

def Training_New_View(request, pk):
    """Displays form for updating the program
    """
    prog = get_object_or_404(Training_Prog, pk=pk)
    if request.method == "POST":
        form = Training_Form(request.POST, instance=prog)
        prog = form.save(commit=False)
        prog.save()
        return redirect('training_detail', pk=prog.pk)
    else:
        form = Program_Edit_Form(instance=computer)
    return render(request, 'WorkforceManagement/Training_Add.html', {'form': form})