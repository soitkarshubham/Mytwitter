from django.urls import path
from .import views

urlpatterns = [
    path('register/',views.registeruser, name = 'register'),
    path('profile-update/',views.profile_update, name = 'profile-update'),
    path('login/',views.loginview, name = 'login'),
    path('logout/',views.logoutview, name = 'logout')
]