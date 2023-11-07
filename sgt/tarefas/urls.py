from django.urls import path
from . import views
urlpatterns = [
   path("",views.tarefas_pendentes_list, name='tarefas_pendentes_list'),
   path('<int:tarefa_id>/concluir/', views.concluir_tarefa, name='concluir_tarefa'),
   path('<int:tarefa_id>/excluir/',views.excluir_tarefa, name='excluir_tarefa'),
   path('<int:tarefa_id>/adiar/', views.concluir_tarefa, name='adiar_tarefa'),
]