from django.urls import path
from . import views
from .views import apod

urlpatterns = [
    path('', views.index, name='space_index'),
    path('apod/', apod, name='space_apod'),
]