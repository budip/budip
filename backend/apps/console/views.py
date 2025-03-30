from django.http import JsonResponse
from .kafka_utils import get_kafka_status

def kafka_status(request):
    return JsonResponse(get_kafka_status())
