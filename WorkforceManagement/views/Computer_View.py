from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from WorkforceManagement.models import Computer


def Computer_List_View(request):
    """Displays all computers in the database"""
    computers = Computer.objects.all()
    return render(request, 'WorkforceManagement/Computer_List.html', {'computers': computers})


def Computer_Detail_View(request, pk):
    computer = get_object_or_404(Computer, pk=pk)
    return render(request, 'WorkforceManagement/Computer_Detail.html', {'computer': computer})
