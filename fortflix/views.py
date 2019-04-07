from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from .models import Movie
from django_downloadview import ObjectDownloadView
import os
# from .models.Movie import basename



default_file_view = ObjectDownloadView.as_view(model=Movie, basename_field = 'basename')

# Create your views here.
def api_main(request):
    pass
    # return render(request, template="", {})

def browse(request):
    # return render(request,,{'movies_list' : Movie.objects.all()})
    pass

def main(request):
    pass

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'