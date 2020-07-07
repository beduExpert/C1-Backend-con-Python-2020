from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("login/",
        auth_views.LoginView.as_view(
            template_name="registration/login.html"),
        name="login"
    ),
    path("logout/", views.logout_user, name="logout_user"),
]
