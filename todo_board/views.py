from django.shortcuts import render

# Create your views here.
from django.views import generic as ge
from todo_main.models import TbTodolist
from .forms import TodoInputForm

class clsTodoBoardMain(ge.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'todo_board/board_main.html'
        todo_datas = TbTodolist.objects.all()
        return render(request, template_name, {"todo_datas":todo_datas})

def fnTodoItemAdd(request):
    template_name = 'todo_board/success.html'
    if request.method == "POST":
        form_data = TodoInputForm(request.POST)
        if form_data.is_valid():
            item = form_data.save(commit=False)
            item.item_save()
            return render(request, template_name, {"msg":"한개의 Todo item을 등록하셨습니다"})
    else:
        template_name = "todo_board/TodoItemAdd.html"
        form = TodoInputForm
        return render(request, template_name, {"form": form})