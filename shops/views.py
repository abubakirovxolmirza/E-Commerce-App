from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import shop

# Create your views here.


class Home(LoginRequiredMixin, ListView):
    model = shop
    template_name = 'shops/index.html'
    context_object_name = 'shop'
    login_url = 'login'


class Message(DetailView):
    model = shop
    template_name = 'shops/message.html'
    context_object_name = 'shop'


class PostShop(CreateView):
    model = shop
    template_name = 'shops/shop.html'
    fields = ['user', 'photo_video', 'shop']
    success_url = '/'


class DeleteShop(DeleteView):
    model = shop
    template_name = 'shops/delete.html'
    success_url = '/'
