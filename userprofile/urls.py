from django.urls import path
from userprofile.views import UserLoginView, UserSignUpView, User_Sign_Up_View, user_logout_view

app_name = "user"

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("register/", User_Sign_Up_View, name="register"),
    path("logout/", user_logout_view, name="logout"),
]
