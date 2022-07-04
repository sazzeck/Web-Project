from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('test', views.test_page, name="test"),
    path('login', views.login_page, name="sing_in"),
    path('registration', views.registration_page, name="sing_up"),
]
