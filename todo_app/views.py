from django.urls import reverse, reverse_lazy

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from todo_app.forms import ListCreateForm, ToDoItemForm, ItemCreateForm
from .models import ToDoItem, ToDoList


class ListListView(ListView):
    model = ToDoList
    template_name = "todo_app/index.html"
    context_object_name = 'todolist_list'


class ItemListView(ListView):
    model = ToDoItem
    template_name = "todo_app/todo_list.html"
    context_object_name = 'todoitems_list'

    def get_queryset(self):
        return ToDoItem.objects.filter(todo_list_id=self.kwargs["list_id"])

    def get_context_data(self):
        context = super().get_context_data()
        context["todo_list"] = ToDoList.objects.get(id=self.kwargs["list_id"])
        return context


class ListCreate(CreateView):
    model = ToDoList
    template_name = "todo_app/todolist_form.html"
    form_class = ListCreateForm

    def get_context_data(self):
        context = super().get_context_data()
        context["title"] = "Add a new list"
        return context

    def get_success_url(self):
        return reverse("todo_app:index")

class ItemCreate(CreateView):
    model = ToDoItem
    form_class = ItemCreateForm

    def get_initial(self):
        initial_data = super().get_initial()
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        initial_data["todo_list"] = todo_list
        return initial_data

    def get_context_data(self):
        context = super().get_context_data()
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        context["todo_list"] = todo_list
        context["title"] = "Create a new item"
        return context

    def get_success_url(self):
        return reverse("todo_app:list", args=[self.object.todo_list_id])


class ItemUpdate(UpdateView):
    model = ToDoItem
    form_class = ToDoItemForm

    def get_context_data(self):
        context = super().get_context_data()
        context["todo_list"] = self.object.todo_list
        context["title"] = "Edit item"
        return context

    def get_success_url(self):
        return reverse("todo_app:list", args=[self.object.todo_list_id])


class ListDelete(DeleteView):
    model = ToDoList
    # You have to use reverse_lazy() instead of reverse(),
    # as the urls are not loaded when the file is imported.
    success_url = reverse_lazy("todo_app:index")


class ItemDelete(DeleteView):
    model = ToDoItem

    def get_success_url(self):
        return reverse_lazy("todo_app:list", args=[self.kwargs["list_id"]])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo_list"] = self.object.todo_list
        return context