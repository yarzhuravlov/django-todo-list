from django.urls import path

from todo.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TagListView,
)

app_name = "todo"
urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("update/<int:pk>", TaskUpdateView.as_view(), name="task-update"),
    path("tags/", TagListView.as_view(), name="tag-list"),
]
