from django.urls import path

from . import views


app_name = 'portfolio'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('resume/', views.ResumeView, name='resume'),
    path('resume_pdf/', views.pdf_view, name='resume_pdf'),
    path('about/', views.AboutView, name='about'),
]