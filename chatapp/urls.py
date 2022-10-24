from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("chatapp", views.frontpage, name="frontpage"),
    path("chatapp/signup/", views.signup, name="signup"),
    path("chatapp/logout/", auth_views.LogoutView.as_view(), name="chatapp_logout"),
    path(
        "chatapp/login/",
        auth_views.LoginView.as_view(template_name="chat-login.html"),
        name="chatapp_login",
    ),
    path("chatapp/rooms/", views.view_rooms, name="rooms"),
    path("chatapp/<slug:slug>/", views.view_room, name="room"),
]
