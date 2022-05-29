from audioop import reverse
import datetime
from unicodedata import category

from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


STATUS = (
    (0, 'Pending'),
    (1, 'Approved')
    )

class BlogPost(models.Model):
    title = models.CharField(max_length=200, unique=False, default='')
    header_image = models.ImageField(null=True, blank=True, upload_to='images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    blogpost_text = RichTextField(blank=True, null=True)
    #blogpost_text = models.TextField(blank=False)
    category = models.CharField(max_length=200, default='Coding')
    snippet = models.CharField(max_length=255, blank=True)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    status = models.IntegerField(choices=STATUS, default=0)


    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def get_absolute_url(self):
        return reverse('blog:index')
        #return reverse('blog:detail', args=(str(self.id)))



class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('blog:index')
        

class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80, blank=True)
    body = models.TextField(blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    snippet = models.CharField(max_length=140, blank=True)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to='images/profile/')
    website_url = models.CharField(max_length=200, null=True, blank=True)
    facebook_url = models.CharField(max_length=200, null=True, blank=True)
    twitter_url = models.CharField(max_length=200, null=True, blank=True)
    instagram_url = models.CharField(max_length=200, null=True, blank=True)
    linkedin_url = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('blog:index')