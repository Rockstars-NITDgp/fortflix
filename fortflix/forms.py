from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'name', 'email', 'mobile')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'name', 'email', 'mobile')

class LoginForm(forms.ModelForm):
    
    class Meta:
        model = CustomUser
        fields = ('username', 'password')