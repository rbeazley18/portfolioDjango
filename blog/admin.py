from django.contrib import admin
from .models import BlogPost, Comment, Category, Profile
from .forms import NewPostForm


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'pub_date')
    
    search_fields = ['title', 'blogpost_text']

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on')
    
    search_fields = ('name', 'body')


admin.site.register(Category)
admin.site.register(BlogPost, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Profile)

    

