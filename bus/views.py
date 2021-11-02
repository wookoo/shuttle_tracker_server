from django.db.models import query
from django.http import JsonResponse


from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
def download(request):
    print("call download")
    return JsonResponse({"status":True})

@csrf_exempt
def upload(request):
    data = JSONParser().parse(request)
    print("call upload")
    print(data)
    return JsonResponse({"status":True})
# Create your views here.
