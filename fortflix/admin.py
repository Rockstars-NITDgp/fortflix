from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Movie

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['name', 'username', 'email', 'mobile', 'coins',]

admin.site.register(CustomUser, CustomUserAdmin)

class CustomMovieAdmin(admin.ModelAdmin):
#    add_form = CustomUserCreationForm
#    form = CustomUserChangeForm
    model = Movie
    list_display = ['name', 'language', 'rating', 'genre', 'release_date']

admin.site.register(Movie, CustomMovieAdmin)
