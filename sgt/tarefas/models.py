from django.db import models
#descrição 
#data de criação
#categoria(urgente,importante,precisa ser feito)
 #statuss(concluido,pendente,adiado)

class Tarefas(models.Model):
    OPCOES_STATUS =(
        ('concluído','Concluido'),
        ('pendente','Pendente'),
        ('Adiado','Adiado'),
    )

    OPCOES_CATEGORIAS =(
        ('urgente','Urgente'),
        ('importante','Importante'),
        ('precisa ser feito','Precisa ser feito'),
    )

    descricao = models.CharField(max_length=400)
    criacao = models.DateTimeField(auto_now_add=True)
    categorias = models.CharField(max_length=25, choices = OPCOES_CATEGORIAS,
                                  default='importante')
    status = models.Charfield(max_length=25, choices = OPCOES_STATUS,
                              default= 'pendente')


