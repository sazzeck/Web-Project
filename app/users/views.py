from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.views.generic import CreateView
from django.shortcuts import redirect
from django.urls import reverse_lazy

from rest_framework.generics import ListAPIView, RetrieveAPIView

from .forms import SingInForm, SingUpForm
from .models import Users
from .serializers import UsersListSerializer, UsersDetailSerializer


class UsersListView(ListAPIView):
    queryset = Users.objects.all()
    serializers = UsersListSerializer


class UserDetailView(RetrieveAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersDetailSerializer


class SingInUser(LoginView):
    form_class = SingInForm
    template_name = "sing_in.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Sing In"
        return context


class SingOutUser(LogoutView):
    next_page = "main"


class SingUpUser(CreateView):
    form_class = SingUpForm
    template_name = "sing_up.html"
    success_url = reverse_lazy("sing_in")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Sing Up"
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("main")


@receiver(user_logged_in)
def got_online(sender, user, request, **kwargs):
    user.is_online = True
    user.save()


@receiver(user_logged_out)
def got_offline(sender, user, request, **kwargs):
    user.is_online = False
    user.save()
