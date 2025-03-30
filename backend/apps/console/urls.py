from django.urls import path
from .views import kafka_status  # ✅ ONLY import what's defined

urlpatterns = [
    path("status/", kafka_status, name="kafka-status"),
]
