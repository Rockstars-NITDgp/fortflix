from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from .models import Movie
from rest_framework import viewsets
from .serializers import MovieSerializer

# Create your views here.
def api_main(request):
    pass

def main(request):
    pass

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'



class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
