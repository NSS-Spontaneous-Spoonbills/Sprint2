from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView, FormView, DetailView, CreateView

from WorkforceManagement.models import Training_Prog

def Training_List_View(request):
    """ Displays all training programs in the company """
    training_progs = Training_Prog.objects.all()
    return render(request, 'WorkforceManagement/Training_List.html', {'training_progs': training_progs})


def Training_Detail_View(request, pk):
    """Displays details about a specific program"""
    prog = get_object_or_404(Training_Prog, pk=pk)
    return render(request, 'WorkforceManagement/Training_Detail.html', {'prog': prog})

def Training_Edit_View(request, pk):
    """Displays form for updating the computers
    Author: Erin Meaker
    """
    computer = get_object_or_404(Computer, pk=pk)
    if request.method == "POST":
        form = Computer_Update_Form(request.POST, instance=computer)
        computer = form.save(commit=False)
        computer.save()
        return redirect('computer_detail', pk=computer.pk)
    else:
        form = Computer_Update_Form(instance=computer)
    return render(request, 'WorkforceManagement/Computer_Update.html', {'form': form})