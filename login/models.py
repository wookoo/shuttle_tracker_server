from django.db import models

class Account(models.Model):
    id = models.CharField(max_length=20,primary_key=True)
    password = models.CharField(max_length=200)
    company = models.CharField(max_length=6)
    phone = models.CharField(max_length=11)
    name = models.CharField(max_length=5)
    type = models.IntegerField() #계정 타입, 회원, 유저 등
    status = models.BooleanField(default=False) #회원가입 여부


