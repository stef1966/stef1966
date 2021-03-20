from django.contrib import admin
from django.urls import path

from . import views

app_name = 'mgc'
urlpatterns = [
    path('', views.IndexPageController, name='index'),
    path('newform', views.CovidForm, name="Formulaire Covid"),
    path('add_form', views.add_Form, name="Formulaire Covid"),
]