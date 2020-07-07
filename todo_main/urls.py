from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'todo_main'

urlpatterns = [
    path('', views.clsTodoMain.as_view(), name='clsTodoMain'),
    path('index', views.clsTodoMain.as_view(), name = 'clsTodoMain'),
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)