from django.db import models

class Account(models.Model):
    id = models.CharField(max_length=20,primary_key=True)
    pw = models.CharField(max_length=200)
    company = models.CharField(max_length=6)
    phone = models.CharField(max_length=11)
    name = models.CharField(max_length=5)
    type = models.IntegerField()


