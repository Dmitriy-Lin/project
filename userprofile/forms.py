from django import forms

from userprofile.models import UserPhoto, Post, CommentPost
from registration.models import User


class PhotoForm(forms.ModelForm):
    class Meta:
        model = UserPhoto
        fields = (
            'photo',
        )
        widgets = {
            "photo": forms.FileInput(attrs={
                                "type": "file",
                                "name": "file",
                                "id": "file",
                                "class": "input-file",
            })
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'body',
            'media',
        )

        widgets = {
            "body": forms.Textarea(attrs={
                            "class": "field__input a-field__input",
                            "placeholder": "Ваш пост",
                            "cols": "40",
                            "rows": "5"
            }),
            'media': forms.FileInput()
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentPost
        fields = (
            'body',
        )

        widgets = {
            "body": forms.TextInput(attrs={
                            "class": "field__input a-field__input",
                            "placeholder": "Ваш комментарий",
                            "style": "height: 40px",
            })
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
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
            if i == "avatar":
                widgets[i] = forms.FileInput(attrs={
                    "type": "file",
                    "name": "file",
                    "id": "file",
                    "class": "input-file",
                })
            elif i == "email":
                widgets[i] = forms.TextInput(attrs={"type": "email", "class": "form-control"})
            elif i == "birth":
                widgets[i] = forms.TextInput(attrs={"type": "date", "class": "form-control"})
            elif i == "man" or i == "woman":
                widgets[i] = forms.CheckboxInput(attrs={"type": "checkbox", "class": "form-check-input"})
            else:
                widgets[i] = forms.TextInput(attrs={"class": "form-control"})
