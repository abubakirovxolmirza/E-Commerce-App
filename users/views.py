from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SignUp
from django.shortcuts import render

# Create your views here.


class Login(LoginView):
    template_name = 'users/login.html'
    next_page = '/'


class Logout(LogoutView):
    next_page = '/'


class UserProfile(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    template_name = 'users/profile.html'

def signup(request):
    if request.method == "POST":
        form = SignUp(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SignUp()
    return render(request, 'users/signup.html', context={'form': form})
