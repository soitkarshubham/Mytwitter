from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from blog.models import Post



PAGINATION_COUNT = 3


def homeview(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html',{'posts':posts})
    
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    paginate_by = PAGINATION_COUNT
    ordering = ['-date_posted']

