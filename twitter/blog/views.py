from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from blog.models import Tweet
from blog.forms import TweetForm


PAGINATION_COUNT = 3


def homeview(request):
    return render(request,'blog/home.html')
    
# class PostListView(ListView):
#     model = Post
#     template_name = 'blog/home.html'
#     context_object_name = 'posts'
#     paginate_by = PAGINATION_COUNT
#     ordering = ['-date_posted']

def tweet_list(request):
    return render(request, 'blog/tweet_list.html', {'object_list': Tweet.objects.all()})

def tweet_new(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, instance = request.user.tweet)
        if form.is_valid():
            form.save()
            return redirect('tweets')
    else:
        form = TweetForm(instance = request.user.author)

    return render(request, 'blog/tweet_new.html', {'form': form })