from django.shortcuts import render, redirect
from django.contrib.auth import login

from django.views.decorators.http import require_GET

from registration.forms import RegistrationForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(
            request.POST, request.FILES
        )
        if form.is_valid():
            user = form.save()
            login(request, user)
            user.verify_email()
            return render(request, "reg/check_email.html")
    else:
        form = RegistrationForm()
    return render(request, "reg/reg.html", context={"form": form})


@require_GET
def verify_email(request):
    key = request.GET.get("key")
    if request.user.check_key(key):
        request.user.is_email_verified = True
        request.user.save()
        return render(request, "reg/account_activated.html")
    return redirect("redirect_user")
