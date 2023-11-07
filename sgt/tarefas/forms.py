from django import forms #importando o pacote forms 
from .models import Tarefas #importando as tarefas da classe tarefa

class AdicionarTarefa(forms.ModelForm):
    class Meta:
        model = Tarefas
        fields = ('descricao','categorias')

class EditarTarefaForm(forms.Form):

  OPCOES_CATEGORIAS =(
        ('urgente','Urgente'),
        ('importante','Importante'),
        ('precisa ser feito','Precisa ser feito'),
    )

  tarefa = forms.Charfield(max_length=400)
  categoria = forms.Charfield(choices=OPCOES_CATEGORIAS)
