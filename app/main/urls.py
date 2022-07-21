from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('test', views.test_page, name="test"),
]
