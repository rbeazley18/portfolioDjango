from unicodedata import name
from django.urls import path

from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('new/', views.NewPostView.as_view(), name ='new_post'),
    path('<int:pk>/comment', views.CommentView.as_view(), name='comment'),
    path('<int:pk>/update', views.UpdatePostView.as_view(), name='update'),
    path('<int:pk>/delete', views.DeletePostView.as_view(), name='delete'),
    path('category/', views.AddCategoryView.as_view(), name ='add_category'),
    path('category-list/', views.CategoryListView, name ='category_list'),
    path('like/<int:pk>', views.LikeView, name='like_post'),
    path('search_blog/', views.SearchBlogView, name='search_blog'),
    path('about/', views.AboutView, name='about'),
    path('category/<str:cats>', views.CategoryView, name ='category'),
]