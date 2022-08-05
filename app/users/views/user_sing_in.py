from django.contrib.auth.views import LoginView

from django.urls import reverse_lazy

from users.forms import SingInForm


class SingInUser(LoginView):
    form_class = SingInForm
    template_name = "users/sing_in.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["title"] = "Sing In"
        return context

    def get_success_url(self):
        return reverse_lazy("main")
