from django.urls import path
from . import views

urlpatterns = [
    path('', views.getPosts, name='blog_post_list'),
    path('categories/', views.getCategories, name='blog_category_list'),
    path('categories/<str:slug>/', views.getCategories, name='blog_category_detail'),
    path('articles/<str:slug>/', views.getPost, name='blog_post_detail')
]
