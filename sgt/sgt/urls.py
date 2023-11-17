from django.contrib import admin
from django.urls import include, path
from tarefas.urls import urlpatterns as tarefas_urls
from usuarios.urls import urlpatterns as usuarios_urls
from usuarios import views
from allauth import urls

urlpatterns = [
    path('',views.cadastro, name = 'cadastro'),
    path('accounts/',include(allauth.urls)),
    path('login/',include(usuarios_urls)),
    path('tarefas/', include(tarefas_urls)),
    
]
