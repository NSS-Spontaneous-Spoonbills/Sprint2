from django.shortcuts import render, get_object_or_404, redirect
from WorkforceManagement.models import Department, Employee
from WorkforceManagement.forms import *

def Department_List_View(request):
    """
    Displays all Departments in the company
    Author: David Paul
    """
    departments = Department.objects.all()
    return render(request, 'WorkforceManagement/Department_list.html', {'departments': departments})

def Department_Detail_View(request, pk):
    """Displays details about a specific department"""
    department = get_object_or_404(Department, pk=pk)
    employees = Employee.objects.all()
    return render(request, 'WorkforceManagement/Department_Detail.html', {'department': department, 'employees': employees})

def Department_New_View(request):
    """Displays form for adding new computer to the database
    Author: David Paul
    """
    if request.method == "POST":
        form = Department_New_Form(request.POST)
        new_comp = form.save(commit=False)
        new_comp.save()
        return redirect('computer_detail', pk=new_comp.pk)
    else:
        form = Department_New_Form()
    return render(request, 'WorkforceManagement/Department_Update.html', {'form': form})


