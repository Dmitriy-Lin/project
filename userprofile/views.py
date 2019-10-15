from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.views.generic import View

from registration.models import User
from userprofile.models import Post, Friends, UserPhoto, CommentPost
from userprofile.form import PhotoForm, PostForm, ProfileForm, CommentForm
from .utils import ListMixin, CreateObjectMixin, UpdateObjectMixin, CreateCommentObjectMixin


def logout_view(request):
    logout(request)
    return redirect("/")


def user(request):
    return redirect("user_page", request.user.id)


class ListUser(ListMixin, View):
    model = User
    template = "userprofile/list_users.html"


class ListFriends(ListMixin, View):
    model = Friends
    template = "userprofile/list_friends.html"


class CreatePost(CreateObjectMixin, View):
    form = PostForm
    template = "userprofile/create_post.html"
    model = Post
    template_alt = "redirect_user"


class UpdatePost(UpdateObjectMixin, View):
    form = PostForm
    template = "userprofile/update_post.html"
    model = Post


class UpdateProfile(UpdateObjectMixin, View):
    form = ProfileForm
    template = "userprofile/update_profile.html"
    model = User


class CreateCommentPost(CreateCommentObjectMixin, View):
    form = CommentForm
    model = Post
    model_alt = CommentPost
    template = "userprofile/comments_post.html"
    template_alt = 'post_comment'


def delete_post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            post_id = request.POST.get('post_id')
            temp = Post.objects.get(pk=post_id)
            temp.delete()
            return redirect("redirect_user")


def userprofile(request, id=None):
        user_data = User.objects.get(id=id)
        post_list = Post.objects.filter(owner_id = id)
        if request.user.is_authenticated:
            if request.method == 'POST':
                user = request.user
                owner = request.POST.get('owner')
                owner = User.objects.get(pk=owner)
                if Friends.objects.filter(owner_id=owner.id, user_id=user.id):
                    pass
                else:
                    Friends.objects.create(owner = owner, user = user).save()
        return render(request, "userprofile/homepage.html",
                    context={
                            "post_list":post_list,
                            "user_data":user_data,
                            "user_id": id
            })


def list_photo(request):
    user = request.user.id
    owner = UserPhoto(user=request.user)
    list_photo = UserPhoto.objects.filter(user_id=user)
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PhotoForm(request.POST, request.FILES, instance=owner)
            if form.is_valid:
                form.save()
                return redirect("list_photo")
        else:
            form = PhotoForm()
            return render(request, "userprofile/photo.html",
                context={
                    "list_photo":list_photo,
                    "form": form
        })
