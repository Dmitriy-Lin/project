from django.urls import path
from . import views

urlpatterns = [
    path('user/logout', views.logout_view, name="logout"),
    path('user/<int:user_id>', views.userprofile, name="user"),
    path('user/post_create', views.post_created, name="post_create")
]
