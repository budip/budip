from django.http import JsonResponse
from django.conf import settings
from django.shortcuts import render
import requests
import json

def index(request):
    return JsonResponse({"message": "Welcome to the NASA API!"})

def apod(request):
    api_url = "https://api.nasa.gov/planetary/apod"
    params = {"api_key": settings.NASA_API_KEY}

    response = requests.get(api_url, params=params)
    data = response.json()

    return JsonResponse(data)
