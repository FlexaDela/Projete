from django import forms #importando o pacote forms 
from .models import Tarefas #importando as tarefas da classe tarefa

class AdicionarTarefa(forms.ModelForm):
    class Meta:
        model = Tarefas
        fields = ('descricao','categorias')