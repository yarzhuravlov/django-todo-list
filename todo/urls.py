from django.urls import path

from todo.views import TaskListView, TaskCreateView, TaskUpdateView

app_name = "todo"
urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("update/<int:pk>", TaskUpdateView.as_view(), name="task-update"),
]
