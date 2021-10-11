from django.db import models
from django.http import request
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, reverse
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from userprofile.forms import CustomUserSignUpForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout




class UserLoginView(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = False
    authentication_form = AuthenticationForm

    def get_success_url(self):
        return reverse("home:main")

class UserSignUpView(CreateView):
    models = User
    form_class = CustomUserSignUpForm
    template_name = "signup.html"

    def form_valid(self,form):
        super().form_valid(form)
        form.save()
        user = authenticate(
            username = form.cleaned_data.get('username'), 
            password = form.cleaned_data.get('password1')
            )
        login(self.request, user)
        return redirect(reverse("home:main"))


    def get_success_url(self):
        return reverse("user:login")

def User_Sign_Up_View(request):
    form = CustomUserSignUpForm(request.POST or None)
    if form.is_valid():
        form.save()
        user = authenticate(
            username = form.cleaned_data.get('username'), 
            password = form.cleaned_data.get('password1')
            )
        login(request, user)
        return redirect(reverse("home:main"))
    return render(request, "signup.html", {"form":form})
    

def user_logout_view(request):
    logout(request) #session destroy
    return redirect(reverse("home:main"))