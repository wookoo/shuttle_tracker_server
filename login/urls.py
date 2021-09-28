from django.urls import path
from .import views

urlpatterns = [
    path("show/",views.show),
    path("register/",views.register),
    path("accept/",views.accept)
]