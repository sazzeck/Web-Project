from django.shortcuts import render


# Create your views here.
def main(request):
    return render(request, "main/main.html", {"title": "Home"})


def test_page(request):
    return render(request, "main/test.html", {"title": "Test"})


def authentication(request):
    return render(request, "main/auth.html", {"title": "Authentication"})


def login_page(request):
    return render(request, "main/login.html", {"title": "Login"})


def registration_page(request):
    return render(request, "main/registration.html", {"title": "Registration"})
