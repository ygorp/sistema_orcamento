from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def fazer_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        senha = request.POST['senha']

        user = authenticate(username=username, password=senha)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')
    return render(request, 'login.html')


@login_required
def home(request):
    return render(request, 'home.html')


def cadastro_usuario(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']

        usuario = User.objects.create_user(
            username=nome,
            email=email,
            password=senha,
            )
        usuario.save()

        return redirect('login')
    return render(request, 'cadastro.html')
