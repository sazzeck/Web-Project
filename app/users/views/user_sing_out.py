from django.contrib.auth.views import LogoutView


class SingOutUser(LogoutView):
    next_page = "main"
