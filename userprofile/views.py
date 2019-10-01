from django.shortcuts import redirect, render
from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return redirect("/")
