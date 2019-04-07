from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from .models import Movie
from django_downloadview import ObjectDownloadView
import os
from rest_framework import viewsets
from .serializers import MovieSerializer
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# from .models.Movie import basename



default_file_view = ObjectDownloadView.as_view(model=Movie, basename_field = 'basename')


# Create your views here.
def api_main(request):
    pass
    # return render(request, template="", {})

@login_required
def browse(request):
    # return render(request,,{'movies_list' : Movie.objects.all()})
    return render(request, 'intro.html')

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


def movie_stream(request, string):
    movie = get_object_or_404(Movie, basename=string)
    print(movie.name)
    print(movie.file.url)
    return render(request, 'movie.html', {'movie':movie,})

def home(request):
    if request.user.is_anonymous:
        return render(request, 'home.html', {})
    else:
        return redirect('browse')

def movies_list(request, page):
    page = int(page)
    limit = int(Movie.objects.all().count())
    if limit< (page*12)+1:
        return redirect('../0')
    ls=[]
    for i in range(page*12+1,min((page*12)+12,limit+1)):
        movie = Movie.objects.get(pk=i)
        ls.append(movie)
    return render(request, 'movie-list.html', {'movies': ls, 'page': page})