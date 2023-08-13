from django.urls import path
from first_app.views import show_task, add_task, edit_task, delete_task, complete_task, completed_tasks

urlpatterns = [
    path('', show_task, name='showTask'),

    path('store_task/', add_task, name='storeTask'),

    path('edit_task/<int:id>/', edit_task, name='editTask'),

    path('delete_task/<int:id>/', delete_task, name='deleteTask'),

    path('complete_task/<int:task_id>/', complete_task, name='completeTask'),

    path('completed_tasks/', completed_tasks, name='completedTask'),

]
 