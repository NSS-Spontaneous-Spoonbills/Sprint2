from django.shortcuts import render
from WorkforceManagement.models import Department

def Department_List_View(request):
    """ Displays all Departments in the company """
    departments = Department.objects.all()
    return render(request, 'WorkforceManagement/Department_list.html', {'departments': departments})

def Department_Detail_View(request, pk):
    """Displays details about a specific department"""
    department = get_object_or_404(department, pk=pk)
    return render(request, 'WorkforceManagement/Department_Detail.html', {'department': department})
