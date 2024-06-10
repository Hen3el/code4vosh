from django.urls import path
from django.conf.urls import url
from django import views as django_views
from . import views
from codes.views import code_choice

app_name = 'main_site'

urlpatterns = [
    url(r'^jsi18n/$', django_views.i18n.JavaScriptCatalog.as_view(), name='jsi18n'),
    path('', views.main_page, name='main'),
    path('lk/', views.pupils_cab, name='lk'),
    path('lk-teacher/', views.teachers_cab, name='lk_teacher'),
]
    #path('entry/<str:token>', views.entry_by_token, name='vosh_redirect')
