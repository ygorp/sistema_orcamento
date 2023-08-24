from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import OrcamentoForm


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
    if request.method == 'POST':
        form = OrcamentoForm(request.POST)
        if form.is_valid():
            nome_cliente = form.cleaned_data['nome_cliente']
            cnpj = form.cleaned_data['cnpj']
            ramo_de_atividade = form.cleaned_data['ramo_de_atividade']
            quantidade_de_cnpj = form.cleaned_data['quantidade_de_cnpj']
            funcionarios_ativos = form.cleaned_data['funcionarios_ativos']
            trabalha_com_escala = form.cleaned_data['trabalha_com_escala']
            utiliza_banco_de_horas = form.cleaned_data['utiliza_banco_de_horas']
            possui_control_id = form.cleaned_data['possui_control_id']
            precisa_aplicativo = form.cleaned_data['precisa_aplicativo']
            precisa_de_facial = form.cleaned_data['precisa_de_facial']
            possui_relogio_inmetro = form.cleaned_data['possui_relogio_inmetro']

            if possui_control_id & precisa_aplicativo:
                sistema_rhid = True
            else:
                sistema_rhid = False

            if possui_relogio_inmetro or possui_control_id & precisa_aplicativo:
                opcoes_orcamento = ['Secullum WEB PRO']
            else:
                opcoes_orcamento = ['Secullum Offline']

            if precisa_aplicativo & possui_control_id or possui_relogio_inmetro & precisa_de_facial:
                opcoes_orcamento = ['Secullum WEB Ultimate']
            else:
                opcoes_orcamento = ['Secullum Offline']
                if precisa_aplicativo:
                    opcoes_orcamento.append('Secullum Web')
                    if funcionarios_ativos > 50 and sistema_rhid:
                        opcoes_orcamento.append('RHID')

            return JsonResponse({'opcoes_orcamento': opcoes_orcamento, 'nome_cliente': nome_cliente, 'cnpj': cnpj})

    return render(request, 'home.html', {'form': OrcamentoForm()})


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
