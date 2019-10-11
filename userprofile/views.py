from django.shortcuts import redirect, render
from django.contrib.auth import logout

from registration.models import User
from userprofile.models import Post, Friends


def logout_view(request):
    logout(request)
    return redirect("/")


def user(request):
    return redirect("user_page", request.user.id)


def userprofile(request, user_id=None):

        user_data = User.objects.get(id=user_id)
        post_list = Post.objects.filter(owner_id = user_id)
        if request.user.is_authenticated:
            if request.method == 'POST':
                user = request.user
                owner = request.POST.get('owner')
                owner = User.objects.get(pk=owner)
                Friends.objects.create(owner = owner, user = user).save()
        return render(request, "userprofile/homepage.html",
                    context={
                            "post_list":post_list,
                            "user_data":user_data,
                            "user_id": user_id
            })


def list_friends(request):
    if request.user.is_authenticated:
        list_friends = Friends.objects.filter(user_id = request.user.id)
        return render(request, "userprofile/list_friends.html",
                    context={
                        "list_friends":list_friends
            })


def list_users(request):
    if request.user.is_authenticated:
        users = User.objects.all()
        return render(request, "userprofile/list_users.html",
                    context={
                        "list_users":users
            })


def post_created(request):
    user_id = request.user.id
    if request.method == "POST":
        body_post = request.POST.get("body_post")
        Post.objects.create(body=body_post, owner_id=user_id)
        return redirect("redirect_user")
    else:
        return render(request, "userprofile/create_post.html")