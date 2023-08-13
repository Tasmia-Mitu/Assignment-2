from django.contrib import admin
from first_app.models import ToDoListModel

# Register your models here. 

class BookStoreModelAdmin(admin.ModelAdmin):
    list_display = ('id','taskTitle', 'taskDescription')


admin.site.register(ToDoListModel, BookStoreModelAdmin)