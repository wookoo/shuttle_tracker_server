from django.db.models import query
from django.http import JsonResponse


from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


lat = 36.76105
lon = 126.91408

tag_dict = {
   "dae9bd80":"이승아",
    "cc1ca216":"신준용",
    "9adbb880":"이찬호",
    "fc7f2d23":"민세리",
    "dc1b7022":"이인구",
    "a99a258d":"윤재욱",
    "696bd8d" : "김기준",
    "8953ca8e":"한정우",
    "d9b1fb8d":"김도현",


}

@csrf_exempt
def gps_download(request):
    print("call download")
    return JsonResponse({"status":True,"lat":lat, "lon":lon})

@csrf_exempt
def gps_upload(request):
    data = JSONParser().parse(request)
    print("call upload")
    data = data['nameValuePairs']
    global lat 
    lat = data['lat']
    global lon
    lon = data['lon']
    return JsonResponse({"status":True})

@csrf_exempt
def ride_upload(request):
    data = JSONParser().parse(request)["nameValuePairs"]
    tag = data['tag']
    try:
        tag = tag_dict[tag]
    except:
        return JsonResponse({"status":False,"name":tag,"info":"123"})

    

    #print("call ride upload")
    #print(data)
    return JsonResponse({"status":True,"name":tag,"info":data["info"]})



@csrf_exempt
def check(request):
    data = JSONParser().parse(request)["nameValuePairs"]
    tags = data['tags']
    tags = tags.rstrip(",").split(",")
    #print(tags)
    #print(data)
    remain = ""
    for i in tags:
        if(i):
            remain += tag_dict[i] +","
    remain = remain.rstrip(",")
    #print(remain)
    return JsonResponse({"status":True,"tags":remain,"remain":data["remain"]})

# Create your views here.
