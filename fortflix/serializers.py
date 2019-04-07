from .models import Movie
from rest_framework import serializers


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ('name', 'description', 'release_date', 'language', 'rating','genre', 'movie_cost', 'rewards','movie_type','movie_length', 'skip_intro')

