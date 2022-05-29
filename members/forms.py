import email
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from blog.models import Profile
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class EditLoginForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class EditProfilePageForm(forms.ModelForm):
    snippet = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Add a short description of yourself that is 140 characters or less...'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Tell us your story...'}))
    profile_pic = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))
    website_url = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    facebook_url = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    twitter_url = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    instagram_url = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    linkedin_url = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ('snippet', 'bio', 'profile_pic', 'website_url', 'facebook_url', 'twitter_url', 'instagram_url', 'linkedin_url')


class CreateProfilePageForm(forms.ModelForm):
    snippet = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Add a short description of yourself that is 140 characters or less...'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Tell us your story...'}))
    profile_pic = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))
    website_url = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    facebook_url = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    twitter_url = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    instagram_url = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    linkedin_url = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ('snippet', 'bio', 'profile_pic', 'website_url', 'facebook_url', 'twitter_url', 'instagram_url', 'linkedin_url')


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')