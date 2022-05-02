from atexit import register
from cProfile import Profile
from re import template
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .forms import *
from django.contrib.auth.views import PasswordChangeView
from blog.models import Profile


class CreateProfilePageView(generic.CreateView):
    model = Profile
    template_name = 'registration/create_user_profile_page.html'
    form_class = CreateProfilePageForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditProfilePageView(generic.UpdateView):
    model = Profile
    form_class = EditProfilePageForm
    template_name = 'registration/edit_profile_page.html'
    
    #def get_success_url(self):

        #return reverse_lazy('members:show_profile_page', kwargs={'pk':self.kwargs['pk']})
    success_url = reverse_lazy('blog:index')


class ShowProfilePageView(generic.DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs): 
        #users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'

    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'

    success_url = reverse_lazy('blog:index')

    def get_object(self):
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    #form_class = PasswordChangeForm
    #success_url = reverse_lazy('blog:index')
    success_url = reverse_lazy('members:password_success')


def password_success(request):
    return render(request, 'registration/password_success.html', {})
