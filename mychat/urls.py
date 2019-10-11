from django.urls import path

from . import views

urlpatterns = [
    path('user/new_chat/<int:recipient>/', views.create_chat, name='create_chat'),
    path('user/chat_room/', views.get_chat_room, name='index'),
    path('user/chat_room/<int:room_name>/', views.room, name='room'),
]
