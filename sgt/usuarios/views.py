from django.shortcuts import render,redirect

def cadastro(request):
    if request.method =='GET':
     return render(request,'cadastro.html')
    else:
       username = request.POST.get()

def login(request):
    return render(request,'login.html')
