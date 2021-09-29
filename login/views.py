from django.db.models import query
from django.http import JsonResponse,HttpResponse
from rest_framework import serializers
from .models import Account
from .serializers import AccountSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

import hashlib

def show(request):
    query_set = Account.objects.filter(status=False,company="123123")
    query_set = Account.objects.all()
    serializer = AccountSerializer(query_set,many=True)
    #query_set = Account.objects.delete
    return JsonResponse(serializer.data, safe=False)

    
@csrf_exempt
def login(request):
     if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            obj = Account.objects.get(id=data['id'])
            password = data['password']
            encrypt = hashlib.sha256(password.encode()).hexdigest()
            serializer = AccountSerializer(obj)
            if encrypt == obj.password: #클라이언트에게 던져줄거정의
                return JsonResponse(serializer.data,status=200)
        except:
            pass
        return JsonResponse({"status":False},status=400)

@csrf_exempt
def register(request):
    #여기서 비밀번호 암호화 진행
    #return JsonResponse({"status":True}, status=200)
    """"""
    if request.method == 'POST':
        print(request)
        data = JSONParser().parse(request)['nameValuePairs']

        password = data['password']
        encrypt = hashlib.sha256(password.encode()).hexdigest()
        data['password'] = encrypt
        serializer = AccountSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            #ok status 전송
            return JsonResponse({"status":True}, status=200)
        else:
            print(data)
            print(serializer.errors)
            return JsonResponse({"status":False}, status=200)

@csrf_exempt
def accept(request): #로그인 승인 ,Account 에 대해 필드 값 변경
    if request.method == 'POST':
        data = JSONParser().parse(request)
        company = data['company']
        query = Account.objects.filter(company=company,status=False)

        serializer = AccountSerializer(query,many=True)
        return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def resetPW(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        name = data['name']
        phone = data['phone']
        id = data['id']
        query = Account.objects.get(id=id,name=name,phone=phone)
        password = data['password']
        encrypt = hashlib.sha256(password.encode()).hexdigest()
        query.password = encrypt
        query.save()
        serializers = AccountSerializer(query)
        return JsonResponse(serializers.data)

@csrf_exempt
def leave(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        