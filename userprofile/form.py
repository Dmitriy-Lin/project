from django import forms

from userprofile.models import UserPhoto, Post, CommentPost
from registration.models import User


class PhotoForm(forms.ModelForm):
    class Meta:
        model = UserPhoto
        fields = (
            'photo',
        )


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'body',
        )


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentPost
        fields = (
            'body',
        )


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
