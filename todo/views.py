from django.urls import reverse_lazy
from django.utils.timezone import now
from django.views import generic

from todo.forms import TaskForm
from todo.models import Task


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["now"] = now()
        context["task_form"] = TaskForm()

        return context


class TaskCreateView(generic.CreateView):
    form_class = TaskForm
    success_url = reverse_lazy("todo:task-list")
