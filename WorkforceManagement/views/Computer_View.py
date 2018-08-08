from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from WorkforceManagement.models import Computer
from WorkforceManagement.forms import Computer_New_Form


def Computer_List_View(request):
    """Displays all computers in the database
    Author: Erin Meaker
    """
    computers = Computer.objects.all()
    return render(request, 'WorkforceManagement/Computer_List.html', {'computers': computers})


def Computer_Detail_View(request, pk):
    """Displays details about a specific computer
    Author: Erin Meaker
    """
    computer = get_object_or_404(Computer, pk=pk)
    return render(request, 'WorkforceManagement/Computer_Detail.html', {'computer': computer})


def Computer_New_View(request):
    """Displays form for adding new computer to the database
    Author: Erin Meaker
    """
    if request.method == "POST":
        form = Computer_New_Form(request.POST)
        new_comp = form.save(commit=False)
        new_comp.save()
        return redirect('computer_detail', pk=new_comp.pk)
    else:
        form = Computer_New_Form()
    return render(request, 'WorkforceManagement/Computer_Update.html', {'form': form})


def Computer_Update_View(request, pk):
    computer = get_object_or_404(Computer, pk=pk)
    if request.method == "POST":
        form = Computer_New_Form(request.POST, instance=post)
        computer = form.save(commit=False)
        computer.save()
        return redirect('computer_detail', pk=computer.pk)
    else:
        form = Computer_New_Form(instance=post)
    return render(request, 'WorkforceManagement/Computer_Update.html', {'form': form})
