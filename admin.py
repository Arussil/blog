from django.contrib import admin
from .models import Post, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

class CategoryToPostInline(admin.TabularInline):
    model = Post.categories.through
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    exclude = ('categories',)
    inlines = [CategoryToPostInline]
