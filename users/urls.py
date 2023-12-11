from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('profile/', views.UserProfile.as_view(), name='profile'),
    path('signup/', views.signup, name='signup'),

]
