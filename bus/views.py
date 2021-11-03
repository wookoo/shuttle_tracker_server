from django.db.models import query
from django.http import JsonResponse


from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
def gps_download(request):
    print("call download")
    return JsonResponse({"status":True})

@csrf_exempt
def gps_upload(request):
    data = JSONParser().parse(request)
    print("call upload")
    print(data)
    return JsonResponse({"status":True})

@csrf_exempt
def ride_upload(request):
    data = JSONParser().parse(request)["nameValuePairs"]
    tag = data['tag']
    if(tag == "dae9bd80"):
        tag = "이승아"
    elif(tag == "cc1ca216"):
        tag = "신준용"
    elif(tag == "9adbb880"):
        tag ="이찬호"
    elif(tag == "fc7f2d23"):
        tag="민세리"
    elif(tag == "dc1b7022"):
        tag = "이인구"
    #if(name == "dae9bd80"):
    #    name = "이승아"
    print("call ride upload")
    print(data)
    return JsonResponse({"status":True,"name":tag,"method":data["method"]})
# Create your views here.
