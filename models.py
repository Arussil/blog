from django.db import models
from django.urls import reverse

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

class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    creation_date = models.DateField(db_index=True, auto_now_add=True)
    categories = models.ManyToManyField(Category, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_post_detail', args=(self.slug,))
