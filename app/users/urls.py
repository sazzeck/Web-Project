from django.urls import path
from .views import SingUpUser, SingInUser, SingOutUser
from .views import UsersListView, UsersDetailView

urlpatterns = [
    path('sing_up', SingUpUser.as_view(), name="sing_up"),
    path('sing_in', SingInUser.as_view(), name="sing_in"),
    path("sing_out", SingOutUser.as_view(), name="sing_out"),

    path("users", UsersListView.as_view()),
    path("user/<int:pk>", UsersDetailView.as_view())
]
