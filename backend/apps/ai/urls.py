from django.urls import path
from .views import chat_ai
from . import views

urlpatterns = [
    path('ping/', views.ping, name='ai_ping'),
    path('chat/', chat_ai, name='chat_ai'),
]