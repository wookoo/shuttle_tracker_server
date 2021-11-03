from django.urls import path
from .import views

urlpatterns = [
    path("gps/upload/",views.gps_upload),
    path("gps/download/",views.gps_download),
    path("ride/upload/",views.ride_upload),
    path("check/",views.check)


]