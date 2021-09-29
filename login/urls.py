from django.urls import path
from .import views

urlpatterns = [
    path("show/",views.show),
    path("register/",views.register),
    path("accept/",views.accept),
    path("resetPW/",views.resetPW),
    path("leave/",views.leave),
    path("login/",views.login),
]