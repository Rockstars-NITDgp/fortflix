from django.urls import path
from django.conf.urls import url
from fortflix import views
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('signup/', views.SignUp.as_view(), name='signup'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
