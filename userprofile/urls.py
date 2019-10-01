from django.urls import path
from . import views

urlpatterns = [
    path('login/logout/', views.logout_view)
]
