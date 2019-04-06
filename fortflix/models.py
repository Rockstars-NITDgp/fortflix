from django.db import models

# Create your models here.
class Movie(models.Model):
    DEFAULT = "DEFAU"
    SCIFI = "SCIFI"
    THRILLERS = "THRILL"
    FAMILY = "FAMIL"
    KIDS = "XKIDS"
    CRIME = "CRIME"
    HORROR = "HORRO"
    ROMANCE = "ROMAN"
    DRAMA = "DRAMA"
    DOCUMENTARY = "DOCUM"
    STANDUP = "STAND"
    ANIME = "ANIME"
    SPORTS = "SPORTS"
    ACTION = "ACTIO"
    AD = "ADVER"
    MOVIE_GENRE_CHOICES = (
        (DEFAULT, 'Default'),
        (SCIFI, 'Science-Fiction'),
        (THRILLERS, 'Thrillers'),
        (FAMILY, 'Family'),
        (KIDS, 'Kids'),
        (CRIME, 'Crime'),
        (HORROR, 'Horror'),
        (ROMANCE, 'Romance'),
        (DRAMA, 'Drama'),
        (DOCUMENTARY, 'Documentary'),
        (STANDUP, 'StandUp Comedy'),
        (AD, 'Advertisement'),
        (ANIME, 'Anime'),
        (SPORTS, 'Sports'),
        (ACTION, 'Action'),
    )
    language = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    rating = models.DecimalField()
    movie_cost = models.IntegerField()
    rewards = models.IntegerField()
    name = models.CharField(max_length=100)
    genre = models.CharField(
        max_length=5,
        choices=MOVIE_GENRE_CHOICES,
        default=DEFAULT,
    )
    release_date = models.DateField()