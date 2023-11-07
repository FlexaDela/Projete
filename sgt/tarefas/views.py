from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefas
from .forms import AdicionarTarefa,EditarTarefaForm

def tarefas_pendentes_list(request):
    tarefas_pendentes = Tarefas.objects.filter(status='pendente')
    if request.method == "POST":
       form = AdicionarTarefa(data=request.POST)
       if form.is_valid():
          form.save()
          return redirect('tarefas_pendentes_list')
    else:
       form = AdicionarTarefa()
    return render(request, 'tarefas/tarefas_pendentes.html',
                  {'tarefas_pendentes':tarefas_pendentes,
                   'form':form})

def concluir_tarefa(request, tarefa_id):
   tarefa = get_object_or_404(Tarefas,id=tarefa_id)
   tarefa.status = 'concluido'
   tarefa.save()
   return redirect('tarefas_pendentes_list')

def excluir_tarefa(request, tarefa_id):
   tarefa = get_object_or_404(Tarefas,id=tarefa_id)
   tarefa.status = 'excluido'
   tarefa.delete()
   return redirect('tarefas_pendentes_list')

def adiar_tarefa(request, tarefa_id):
   tarefa = get_object_or_404(Tarefas,id=tarefa_id)
   tarefa.status = 'adiado'
   tarefa.save()
   return redirect('tarefas_pendentes_list')

def editar_tarefa(request, tarefa_id):
   tarefa= get_object_or_404(Tarefas, id=tarefa_id)
   if request.method == 'POST':
      form = EditarTarefaForm(request.POST)
      if form.is_valid():
         cd = form.cleaned_data