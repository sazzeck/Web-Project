from django.urls import path
from . import views

urlpatterns = [
    path('registration', views.SingUpUser.as_view(), name="sing_up"),
    path('login', views.SingInUser.as_view(), name="sing_in"),
    path("singout", views.singout_user, name="sing_out"),
]
