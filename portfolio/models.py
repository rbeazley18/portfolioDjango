from tabnanny import verbose
from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.urls import reverse


class Projects(models.Model):
    order = models.IntegerField(default='1')
    title = models.CharField(max_length=200, unique=True)
    header_image = models.ImageField(null=True, blank=True, upload_to='images/projects')
    author = models.CharField(max_length=200,)
    pub_date = models.DateTimeField(auto_now_add=True)
    snippet = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=False)
    website_url = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Project'
