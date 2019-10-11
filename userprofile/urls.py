from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.user, name='redirect_user'),
    path('user/logout', views.logout_view, name="logout"),
    path('user/<int:user_id>', views.userprofile, name="user_page"),
    path('user/friends', views.list_friends, name="list_friends"),
    path('user/list_users', views.list_users, name="list_users"),
    path('user/post_create', views.post_created, name="post_create")
]