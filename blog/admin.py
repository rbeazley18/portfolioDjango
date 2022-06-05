from django.contrib import admin
from .models import BlogPost, Comment, Profile
from .forms import NewPostForm


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'category', 'pub_date')
    list_filter = ('status', 'category')
    search_fields = ['title', 'blogpost_text']

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on')
    
    search_fields = ('name', 'body')



admin.site.register(BlogPost, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Profile)

    

