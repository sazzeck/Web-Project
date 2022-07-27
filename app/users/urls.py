from django.urls import path
from . import views

urlpatterns = [
    path('sing_up', views.SingUpUser.as_view(), name="sing_up"),
    path('sing_in', views.SingInUser.as_view(), name="sing_in"),
    path("sing_out", views.SingOutUser.as_view(), name="sing_out"),
    path("users", views.UsersListView.as_view()),
    path("users/<int:pk>", views.UserDetailView.as_view())
]
