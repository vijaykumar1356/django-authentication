from django.urls import path
from .views import home_view, login_view, register_view, logoutUser
urlpatterns = [
    path("", home_view, name="home"),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logoutUser, name="logout")
]