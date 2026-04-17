from django.http import request
from blog.models import Blog, Category
from django.shortcuts import render, get_object_or_404


def post_by_category(request, category_id):
    posts = Blog.objects.filter(category_id=category_id, status=1)
    category = get_object_or_404(Category, id=category_id)
    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'post_by_category.html', context)