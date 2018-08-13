from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView, FormView, DetailView, CreateView

from WorkforceManagement.forms import Training_New_Form
from WorkforceManagement.models import Training_Prog

def Training_List_View(request):
    """ Displays all training programs in the company """
    training_progs = Training_Prog.objects.all()
    return render(request, 'WorkforceManagement/Training_List.html', {'training_progs': training_progs})


def Training_Detail_View(request, pk):
    """Displays details about a specific program"""
    prog = get_object_or_404(Training_Prog, pk=pk)
    return render(request, 'WorkforceManagement/Training_Detail.html', {'prog': prog})

class Training_Form_View(FormView):
    """Displays form for updating the program
    """
    template_name = 'WorkforceManagement/Training_Form.html'
    form_class = Training_New_Form
    success_url = '/WorkforceManagement/training_programs'

    def form_valid(self, form):

        form.save()
        return super(Training_Form_View, self).form_valid(form)

    # if request.method == "POST":
    #     form = Training_Form(request.POST)
    #     add_prog = form.save(commit=False)
    #     add_prog.save()
    #     return redirect('training_detail', pk=add_prog.pk)
    # # else:
    # #     form = Training_Form()
    #     return render(request, 'WorkforceManagement/Training_Add.html', {'form': form})