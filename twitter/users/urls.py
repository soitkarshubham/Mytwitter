from django.urls import path
from .import views

urlpatterns = [
    path('register/',views.registeruser, name = 'register'),
    path('profile/',views.profile, name = 'update-profile'),
    path('login/',views.loginview, name = 'login'),
    path('logout/',views.logoutview, name = 'logout')
]