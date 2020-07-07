from django.shortcuts import render

# Create your views here.
from django.views import generic as ge
from .models import TbTodolist

class clsTodoMain(ge.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'todo_main/board_main.html'
        todo_datas = TbTodolist.objects.all()
        return render(request, template_name, {"todo_datas":todo_datas})

