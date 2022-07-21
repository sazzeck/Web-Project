from django.urls import path
from . import views

urlpatterns = [
    path('login', views.LoginUser.as_view(), name="sing_in"),
    path('registration', views.RegisterUser.as_view(), name="sing_up"),
]
