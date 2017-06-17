from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.getPosts, name='blog_post_list'),
    url(r'^categories/$', views.getCategories, name='blog_category_list'),
    url(r'^categories/(?P<slug>[-\w]+)/$', views.getCategory, name='blog_category_detail'),
    url(r'^(?P<slug>[-\w]+)/$', views.getPost, name='blog_post_detail'),
]
