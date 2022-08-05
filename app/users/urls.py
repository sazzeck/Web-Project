from django.urls import path
from .views import SingUpUser, SingInUser, SingOutUser

urlpatterns = [
    path('sing_up', SingUpUser.as_view(), name="sing_up"),
    path('sing_in', SingInUser.as_view(), name="sing_in"),
    path("sing_out", SingOutUser.as_view(), name="sing_out"),
]
