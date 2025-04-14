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


class TagForm(forms.ModelForm):
    id = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "type": "hidden",
                "id": "tagIdInput",
            }
        ),
    )
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "id": "tagNameInput",
            },
        )
    )

    class Meta:
        model = Tag
        fields = "__all__"
