from django.core.validators import MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


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
    BASIC = "BASIC"
    PAID = "PAID"
    MOVIE_TYPE = (
        (BASIC, 'Basic'),
        (PAID, 'Paid')
    )
    language = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    rating = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
    )
    file = models.FileField(upload_to='uploads/', max_length=100, default='uploads/default.jpeg')
    movie_cost = models.IntegerField()
    rewards = models.IntegerField()
    name = models.CharField(max_length=100)
    genre = models.CharField(
        max_length=15,
        choices=MOVIE_GENRE_CHOICES,
        default=DEFAULT,
    )
    release_date = models.DateField()
    movie_type = models.CharField(max_length=5, choices=MOVIE_TYPE, default='Paid')
    movie_length = models.TimeField()
    skip_intro = models.TimeField()
    #Attributes required for serving files
    basename = models.CharField(max_length=100, default="0")
    slug = models.SlugField(max_length=50, default="none")


class CustomUser(AbstractUser):
    name = models.CharField(max_length=30)
    mobile = models.IntegerField(validators=[MaxValueValidator(9999999999)], null=True)
    coins = models.IntegerField(default=0)

    def __str__(self):
        return self.name
