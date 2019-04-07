"""ffproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf.urls import url, include
from fortflix import views
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .models import Movie
from django_downloadview import ObjectDownloadView
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'movies', views.MovieViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    #path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('browse', views.browse, name='browse'),
    path('movies_list', views.movies_list, name='movies_list'),
    path('', views.home, name='home'),
    path('stream/<str : movie>', views.default_file_view, name='default_file_view'),
    path('stream/<slug>/', views.default_file_view, name='default_file_view'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    # url(r'^logout/$', 'django.contrib.auth.views.logout',{'next_page': '/home/'}, name='logout'),
    path('api/', include(router.urls)),
    url(r'^movie/(?P<string>[ \w\-]+)/$', views.movie_stream, name='movie_stream')
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
