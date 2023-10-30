from django.urls import path
from tarefas.views import index
urlpatterns = [
   path("",index)
]