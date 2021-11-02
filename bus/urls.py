from django.urls import path
from .import views

urlpatterns = [
    path("upload/",views.show),
    path("download/",views.register),


]