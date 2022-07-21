from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RegisterUserForm, LoginUserForm


# Create your views here.


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "login.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Login"
        return context


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "registration.html"
    success_url = reverse_lazy("sing_in")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Registeration"
        return context
