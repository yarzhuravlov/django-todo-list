from django.utils.timezone import now
from django.views import generic

from todo.models import Task


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["now"] = now()

        return context
