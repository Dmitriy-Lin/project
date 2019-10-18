from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.user, name='redirect_user'),
    path('user/logout', views.logout_view, name="logout"),
    path('user/<int:id>', views.userprofile, name="user_page"),
    path('user/friends', views.ListFriends.as_view(), name="list_friends"),
    path('user/profile_update/<int:id>', views.UpdateProfile.as_view(), name="profile_update"),
    path('user/list_users', views.ListUser.as_view(), name="list_users"),
    path('user/list_users/search', views.search, name="list_users_search"),
    path('user/<int:id>/photo', views.OtherUserPhoto.as_view(), name="other_user_photo"),
    path('user/post_create', views.CreatePost.as_view(), name="post_create"),
    path('user/post/<int:id>', views.UpdatePost.as_view(), name="post_update"),
    path('user/post/<int:id>/comment', views.CreateCommentPost.as_view(), name="post_comment"),
    path('user/delete_post/<int:post_id>', views.delete_post, name="delete_post"),
    path('user/photo', views.list_photo, name="list_photo")
]
