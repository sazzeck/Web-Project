from django.views.generic import CreateView

from django.urls import reverse_lazy
from django.shortcuts import redirect

from django.contrib.auth import login


from users.forms import SingUpForm


class SingUpUser(CreateView):
    form_class = SingUpForm
    template_name = "users/sing_up.html"
    success_url = reverse_lazy("sing_in")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["title"] = "Sing Up"
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("main")
