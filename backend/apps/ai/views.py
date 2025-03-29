from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .services import get_openai_response


def ping(request):
    return JsonResponse({'message': 'AI app is alive!'})

@csrf_exempt
def chat_ai(request):
    if request.method == "POST":
        body = json.loads(request.body)
        prompt = body.get("prompt", "")

        if not prompt:
            return JsonResponse({"error": "Prompt is required"}, status=400)

        response = get_openai_response(prompt)
        return JsonResponse({"response": response})

    return JsonResponse({"error": "Invalid method"}, status=405)

@csrf_exempt
def analyze_image(request):
    if request.method == "POST":
        image_file = request.FILES.get("image")
        if not image_file:
            return JsonResponse({"error": "No image file provided"}, status=400)

        from .services import get_openai_response_image_analyzer  # or wherever you defined it
        result = get_openai_response_image_analyzer(image_file)
        return JsonResponse({"result": result})

    return JsonResponse({"error": "Invalid method"}, status=405)
