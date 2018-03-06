from django.conf import settings
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

from tinymce import HTMLField

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_category_detail', args=(self.slug,))

def deleted_author():
    """
    Used if we an author get deleted and we want to keep the posts
    """
    return get_user_model().objects.get_or_create(username='deleted')[0]

class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(deleted_author)
    )
    slug = models.SlugField(max_length=100, unique=True)
    body = HTMLField()
    creation_date = models.DateField(db_index=True, auto_now_add=True)
    categories = models.ManyToManyField(Category, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('blog_post_detail', args=(self.slug,))

    def get_author(self):
        if self.author.get_full_name():
            return self.author.get_full_name()
        return 'Anonymus'

    class Meta:
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title

