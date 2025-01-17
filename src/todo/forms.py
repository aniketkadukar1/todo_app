from django import forms
from .models import Task


class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline']
        widgets = {
        'title': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter task title',
        }),
        'description': forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter task description (optional)',
            'rows': 3,
        }),
        'deadline': forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date',
        }),
}