from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView, FormView, DetailView, CreateView
from WorkforceManagement.models.Training_Model import Training_Prog

# from history.forms import ArtistForm



class Training_List_View(ListView):
  model = Training_Prog
  # Django defaults to referencing the data in the template as 'object_list'. Here is how we can rename it what we want
  context_object_name = 'prog_list'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["location"] = "artists"
    return context

class ArtistFormView(FormView):
  template_name = 'history/artist_form.html'
  form_class = ArtistForm
  # NOTE! Be sure to put the slash in front of the url to route properly
  success_url = '/history/artists/'

  def form_valid(self, form):
    # This method is called when valid form data has been POSTed.
    # It should return an HttpResponse.
    form.save()
    return super(ArtistFormView, self).form_valid(form)

# With a detail view you only need to provide the model. Django does everything else (as long as you've named your template `artist_detail`) But we want to also include all of the Artist's songs, to. So we have to add them to the context object that's bound to the template
class ArtistDetailView(DetailView):
      model = Artist