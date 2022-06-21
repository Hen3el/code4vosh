from django.urls import path
from . import views

app_name = 'main_site'

urlpatterns = [
    path('', views.main, name='main'),
]
