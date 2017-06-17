from django.shortcuts import render
from django.http import HttpResponse

from .models import Post, Category

def getPosts(request):
    posts = Post.objects.order_by('-creation_date')
    context = {'post_list': posts}
    return render(request, 'blog/post_list.html', context)

def getPost(request, slug):
    post = Post.objects.get(slug=slug)
    categories = post.categories.all
    context = {
        'post': post,
        'categories': categories
    }
    return render(request, 'blog/post_detail.html', context)

def getCategories(request):
    categories = Category.objects.all()
    context = {'category_list': categories}
    return render(request, 'blog/category_list.html', context)

def getCategory(request, slug):
    category = Category.objects.get(slug=slug)
    posts = category.post_set.all
    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'blog/category_detail.html', context)
