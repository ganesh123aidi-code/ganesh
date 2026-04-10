
from django.shortcuts import render
from blog.models import Blog


def home(request):
    featured_posts = Blog.objects.filter(featured_post=True, status=1).order_by('-created_at')
    posts=Blog.objects.filter(status=1).order_by('-created_at')
    breaking_news = Blog.objects.filter(featured_post=False, status=1).order_by('-created_at')[:5]
    context = {
        'featured_posts': featured_posts,
        'posts': posts,
        'breaking_news': breaking_news,
    }
    return render(request, 'home.html', context)