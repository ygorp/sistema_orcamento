from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Usuario


def fazer_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        
        user = authenticate(request, email=email, senha=senha)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')


def home(request):
    return render(request, 'home.html')


def cadastro_usuario(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']
     
        usuario = Usuario(nome=nome, email=email, senha=senha)
        usuario.save()

        return redirect('login')
    return render(request, 'cadastro.html')
