from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.contrib.auth import login

from django.views.generic import CreateView

from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.dispatch import receiver

from users.forms import SingInForm, SingUpForm


class SingInUser(LoginView):
    form_class = SingInForm
    template_name = "users/sing_in.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Sing In"
        context["navbar_title"] = "Home"
        return context

    def get_success_url(self):
        return reverse_lazy("main")


class SingOutUser(LogoutView):
    next_page = "main"


class SingUpUser(CreateView):
    form_class = SingUpForm
    template_name = "users/sing_up.html"
    success_url = reverse_lazy("sing_in")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Sing Up"
        context["navbar_title"] = "Home"
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
