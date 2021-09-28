from django.db.models import query
from django.http import JsonResponse,HttpResponse
from rest_framework import serializers
from .models import Account
from .serializers import AccountSerializer
from rest_framework.parsers import JSONParser

def show(request):
    query_set = Account.objects.all()
    serializer = AccountSerializer(query_set,many=True)
    #query_set = Account.objects.delete
    return JsonResponse(serializer.data, safe=False)


def register(requst):
    #여기서 비밀번호 암호화 진행
    """"""
    serializer = AccountSerializer(data={"id":"user",
    "pw":"12345",
    "company":"123456",
    "phone":"01012345678",
    "name":"엄준식",
    "type":1})
    if serializer.is_valid():
        serializer.save()
        #ok status 전송
        return JsonResponse(serializer.data, status=201)
    else:

        return JsonResponse(serializer.errors, status=400)

def accept(request): #로그인 승인 ,Account 에 대해 필드 값 변경
    
    query = Account.objects.get(id="user")
    query.pw ="4567" #비밀번호 업데이트
    query.save()
    serializer = AccountSerializer(query)
    return JsonResponse(serializer.data)
