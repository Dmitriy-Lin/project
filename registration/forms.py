from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
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
            "number_phone",
            "avatar"
        )

        widgets = {}

        for i in fields:
            if i != "avatar":
                if i == "email":
                    widgets[i] = forms.TextInput(attrs={"type": "email", "class": "form-control"})
                elif i == "birth":
                    widgets[i] = forms.TextInput(attrs={"type": "date", "class": "form-control"})
                elif i == "man" or i == "woman":
                    widgets[i] = forms.CheckboxInput(attrs={"type": "checkbox", "class": "form-check-input"})
                elif i == "password":
                    widgets[i] = forms.PasswordInput(attrs={"class": "form-control"})
                else:
                    widgets[i] = forms.TextInput(attrs={"class": "form-control"})

    def clean(self):
        if validate_password(self.cleaned_data['password']):
            pass
        return self.cleaned_data

    def save(self, commit=True):
        password = (
            make_password(self.cleaned_data['password'])
        )
        self.instance.password = password
        self.cleaned_data['password'] = password
        return super().save(commit)
