from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'todo_board'

urlpatterns = [
    #path('', views.clsTodoBoardMain.as_view(), name='clsTodoBoardMain'),
    path('add/', views.fnTodoItemAdd, name='fnTodoItemAdd'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)