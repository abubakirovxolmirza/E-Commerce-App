from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='index'),
    path('shop/<int:pk>', views.Message.as_view(), name='message'),
    path('new/', views.PostShop.as_view(), name='new'),
    path('shop/<int:pk>/delete', views.DeleteShop.as_view(), name='delete'),
]