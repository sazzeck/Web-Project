from django.urls import path
from . import views

urlpatterns = [
    path('login', views.LoginUser.as_view(), name="sing_in"),
    path("singout", views.singout_user, name="sing_out"),
    path('registration', views.RegisterUser.as_view(), name="sing_up"),
]
