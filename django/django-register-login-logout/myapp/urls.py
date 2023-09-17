from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),  # Custom login view
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Django's built-in logout view
]