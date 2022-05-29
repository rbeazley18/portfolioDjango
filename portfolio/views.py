from pyexpat import model
from django.shortcuts import render
from django.http import HttpResponseRedirect, FileResponse, HttpResponse
import os
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone

from .models import Projects


class IndexView(generic.ListView):
    model = Projects
    template_name = 'portfolio/index.html'
    context_object_name = 'project_list'

    def get_queryset(self):
        return Projects.objects.all().order_by('order')


class DetailView(generic.DetailView):
    model = Projects
    template_name = 'portfolio/detail.html'


def ResumeView(request):
    return render(request, 'portfolio/resume.html')

def pdf_view(request):
    with open('static/resume.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(),content_type='application/pdf')
        response['Content-Disposition'] = 'filename=some_file.pdf'
        return response


def AboutView(request):
    return render(request, 'portfolio/about.html')

    
