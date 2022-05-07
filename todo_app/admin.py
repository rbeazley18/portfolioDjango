from django.contrib import admin
from todo_app.models import ToDoItem, ToDoList

class ToDoListAdmin(admin.ModelAdmin):
    list_display = ('title')
    search_fields = ('title')

class ToDoItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_date', 'due_date', )
    search_fields = ('title')

admin.site.register(ToDoItem)
admin.site.register(ToDoList)


