from django import forms
from .models import BlogPost, Comment

#choices = [('coding', 'coding'), ('sports', 'sports'), ('movies', 'movies'),]



class NewPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'blogpost_text', 'snippet', 'header_image')

        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control'}),
            'blogpost_text':forms.Textarea(attrs={'class': 'form-control'}),
            'snippet':forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Add a short description of your post'}),
        }


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'blogpost_text', 'snippet')

        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control'}),
            'blogpost_text':forms.Textarea(attrs={'class': 'form-control'}),
            'snippet':forms.Textarea(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name':forms.TextInput(attrs={'class': 'form-control'}),
            'body':forms.Textarea(attrs={'class': 'form-control'}),
        }
