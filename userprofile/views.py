from django.shortcuts import redirect, render
from django.contrib.auth import logout

from registration.models import User
from userprofile.models import Post


def logout_view(request):
    logout(request)
    return redirect("/")


def userprofile(request, user_id=None):
    if request.user.is_authenticated:
        user_data = User.objects.get(id=user_id)
        post_list = Post.objects.filter(owner_id=user_id)
        return render(request, "userprofile/homepage.html",
                      context={"user_id": user_id,
                               "post_list": post_list,
                               "user_data": user_data
                               })


def post_created(request):
    user_id = request.user.id
    if request.method == "POST":
        body_post = request.POST.get("body_post")
        Post.objects.create(body=body_post, owner_id=user_id)
        return redirect("user", user_id)
    else:
        return render(request, "userprofile/create_post.html")

