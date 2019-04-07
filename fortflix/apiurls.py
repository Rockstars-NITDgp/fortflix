# """ffproj URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/2.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.urls import path, include
# #from django.contrib.auth.models import CustomUser
# from rest_framework import routers, serializers, viewsets
# from . import views
# from . models import Movie
# from django.contrib.auth.decorators import login_required
# from rest_framework.decorators import action


# class MovieSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Movie
#         fields = ('name', 'genre', 'release_date')


# class MovieDetailedSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Movie
#         fields = (each.name for each in Movie._meta.get_fields())

# @login_required
# class MovieViewSet(viewsets.ModelViewSet):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer


# # @login_required
# # class MovieDetailedViewSet(viewsets.ModelViewSet):
# #         # movie_details = Movie.objects.get(name=moviename)
# #         # serializer_class = MovieDetailedSerializer
# #         def Moviedetails(self, request, moviename):
# #             movie_details = Movie.objects.get(name=moviename)
# #             serializer_class = MovieDetailedSerializer

# router = routers.DefaultRouter()
# router.register('$', MovieViewSet)
# # router.register('movie/{moviename}/$', MovieDetailedViewSet, base_name='movie')



# urlpatterns += router.urls