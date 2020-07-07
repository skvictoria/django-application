from django import forms
from todo_main.models import TbTodolist

class TodoInputForm(forms.ModelForm):
    class Meta:
        model = TbTodolist
        fields = ('todo_title', 'todo_contents')