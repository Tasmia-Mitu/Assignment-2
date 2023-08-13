from django import forms 
from first_app.models import ToDoListModel
 
class ToDoListForm(forms.ModelForm):
    class Meta:
        model = ToDoListModel
        fields = ['taskTitle', 'taskDescription']