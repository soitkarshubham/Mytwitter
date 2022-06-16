from django.urls import path
from .import views

urlpatterns = [
    path('home/',views.homeview, name = 'home'),
    path('tweets/',views.tweet_list, name = 'tweets'),
    path('new-tweet/',views.tweet_new, name = 'new-tweet'),
]