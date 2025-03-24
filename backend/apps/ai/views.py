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
