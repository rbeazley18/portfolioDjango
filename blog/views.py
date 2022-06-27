from operator import contains
from unicodedata import category
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone

from .models import BlogPost, Comment
from .forms import NewPostForm, CommentForm, UpdatePostForm
 
 
class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_blogpost_list'

    def get_queryset(self):
        return BlogPost.objects.filter(status=1).order_by('-pub_date')

    
 


class DetailView(generic.DetailView):
    model = BlogPost
    template_name = 'blog/detail.html'

    #def get_queryset(self):
        #"""
        #Excludes any blogposts that aren't published yet.
        #"""
        #return BlogPost.objects.filter(pub_date__lte=timezone.now())

    def get_context_data(self, *args, **kwargs): 
        context = super(DetailView, self).get_context_data(*args, **kwargs)

        the_likes = get_object_or_404(BlogPost, id=self.kwargs['pk'])
        total_likes = the_likes.total_likes()

        liked = False
        if the_likes.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['total_likes'] = total_likes
        context['liked'] = liked
        return context


def LikeView(request, pk):
    post = get_object_or_404(BlogPost, id=request.POST.get('blogpost_id'))
    liked = False

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('blog:detail', args=[str(pk)]))


class NewPostView(generic.CreateView):
    model = BlogPost
    form_class = NewPostForm
    template_name = 'blog/new_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePostView(generic.UpdateView):
    model = BlogPost
    form_class = UpdatePostForm
    template_name = 'blog/update_post.html'

    def get_success_url(self):
        return reverse_lazy('blog:detail', kwargs={'pk':self.kwargs['pk']})

    


class DeletePostView(generic.DeleteView):
    model = BlogPost
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('blog:index')

    


class CommentView(generic.CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blog:detail', kwargs={'pk':self.kwargs['pk']})

    


def SearchBlogView(request):

    if request.method == 'POST':
        searched = request.POST['searched']
        blogs = BlogPost.objects.filter(title__contains=searched)
        return render(request, 'blog/search_blog.html', {'searched':searched, 'blogs':blogs})
    else:
        return render(request, 'blog/search_blog.html', {})


def AboutView(request):
    return render(request, 'blog/about.html')




        
