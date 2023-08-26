from django.urls import path
from .views import my_login, profile

urlpatterns = [
    path("myauth/", my_login, name="login"),
    path("profile/", profile, name="profile"),
]