from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET

from registration.form import RegistrationForm
from registration.models import User


def login_view(request):
    if request.method == 'GET':
        return render(request, "auth.html", context={
            "error": False
        })
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(
            username=username,
            password=password
        )
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            try:
                user = User.objects.get(username=username)
                user.incorrect_attempts += 1
                if user.incorrect_attempts > settings.INCORRECT_ATTEMPTS_LIMIT:
                    user.is_active = False
                user.save()
            except User.DoesNotExist:
                pass
            return render(request, "auth.html", context={
                "error": True
            })


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(
            request.POST
        )
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, "userprofile/homepage.html")
    else:
        form = RegistrationForm()
    return render(request, "reg/reg.html", context={"form": form})
