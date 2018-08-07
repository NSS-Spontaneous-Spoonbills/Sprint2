from django import HttpResponse
from WorkforceManagement.models import Department

def Department_List_View(request):
    """ Displays all Departments in the company """
    departments = Department.objects.all()
    return render(request, 'WorkforceManagement/Department_list.html', {'departments': departments})
