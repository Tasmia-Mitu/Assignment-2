from django.shortcuts import render, redirect
from first_app.forms import ToDoListForm
from first_app.models import ToDoListModel

# Create your views here.
def add_task(request):
    if request.method == 'POST':
        list = ToDoListForm(request.POST)
        if list.is_valid():
            list.save()
            print(list.cleaned_data)
            return redirect('showTask')
    else:
        list = ToDoListForm()

    return render(request, 'store_task.html', {'form':list})

def show_task(request):
    list = ToDoListModel.objects.filter(is_completed=False)
    print(list)
    return render(request, 'show_task.html', {'data':list})

def edit_task(request, id):
    task = ToDoListModel.objects.get(pk=id)
    form = ToDoListForm(instance = task)

    if request.method == 'POST':
        form = ToDoListForm(request.POST, instance = task)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect ('showTask')
    else:
        form = ToDoListForm(instance=task)

    return render(request, 'edit_task.html', {'form' : form})


def delete_task(request, id):
    list = ToDoListModel.objects.get(pk = id)
    list.delete()
    return redirect('showTask')

def complete_task(request, task_id):
    task = ToDoListModel.objects.get(pk=task_id)
    task.is_completed = True
    task.save()
    return redirect('completedTask')

def completed_tasks(request):
    tasks = ToDoListModel.objects.filter(is_completed=True)
    return render(request, 'completed_tasks.html', {'tasks': tasks})