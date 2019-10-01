from django import forms
from django.contrib.auth.hashers import make_password

from registration.models import User


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "city",
            "country",
            "address",
            "birth",
            "man",
            "woman",
            "number_phone"
        )

        widgets = {}

        for i in fields:
            widgets[i] = forms.TextInput(attrs={"class": "form-control"})
            if i == "email":
                widgets[i] = forms.TextInput(attrs={"type": "email", "class": "form-control"})
            elif i == "birth":
                widgets[i] = forms.TextInput(attrs={"type": "date", "class": "form-control"})
            elif i == "man" or i == "woman":
                widgets[i] = forms.CheckboxInput(attrs={"type": "checkbox", "class": "form-check-input"})
            elif i == "password":
                widgets[i] = forms.TextInput(attrs={"type": "password", "class": "form-control"})

    def save(self, commit=True):
        password = (
            make_password(
                self.cleaned_data['password']
            )
        )
        self.instance.password = password
        self.cleaned_data['password'] = password
        return super().save(commit)
