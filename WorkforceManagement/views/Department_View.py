from django import HttpResponse

def Department_List_View(request):
    """ Displays all Departments in the company """
    departments = Departments.objects.all()
    return render(request, 'WorkforceManagement/Department_list.html', {'departments': departments})
