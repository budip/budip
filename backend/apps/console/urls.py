from django.urls import path
from .views import kafka_status

urlpatterns = [
    path("status/", kafka_status, name="kafka-status"),
]
