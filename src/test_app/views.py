from django.http import JsonResponse
from datetime import datetime

def time(request):
    return JsonResponse({"time": str(datetime.now())})