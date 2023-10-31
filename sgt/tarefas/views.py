from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Tarefa

def tarefas_pendentes_list(request):
    tarefas_pendentes = Tarefa.objects.filter(status='pendente')
    return render(request, 'tarefas/tarefas_pendentes.html',
                  {'tarefas_pendentes':tarefas_pendentes})