from django import forms

from todo.models import Task, Tag


class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(
            attrs={"type": "datetime-local"},
        ),
    )
    content = forms.CharField(
        label="What do you need to do?",
        widget=forms.Textarea(attrs={"rows": 3}),
    )
    tags = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
    )

    class Meta:
        model = Task
        exclude = ["created_at", "is_completed"]
