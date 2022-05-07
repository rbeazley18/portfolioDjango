from django import forms
from .models import ToDoItem, ToDoList


class ListCreateForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ('title',)

        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control'}),
        }


class ToDoItemForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = ('todo_list', 'title', 'description', 'due_date')

        widgets = {
            'todo_list':forms.Select(attrs={'class': 'form-control'}),
            'title':forms.TextInput(attrs={'class': 'form-control'}),
            'description':forms.Textarea(attrs={'class': 'form-control'}),
            'due_date':forms.TextInput(attrs={'class': 'form-control'}),
        }

class ItemCreateForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = ('todo_list', 'title', 'description', 'due_date')

        widgets = {
            'todo_list':forms.Select(attrs={'class': 'form-control'}),
            'title':forms.TextInput(attrs={'class': 'form-control'}),
            'description':forms.Textarea(attrs={'class': 'form-control'}),
            'due_date':forms.TextInput(attrs={'class': 'form-control'}),
        }