from django import forms


class OrcamentoForm(forms.Form):
    nome_cliente = forms.CharField(max_length=100)
    cnpj = forms.CharField(max_length=20)
    ramo_de_atividade = forms.CharField(max_length=40)
    quantidade_de_cnpj = forms.IntegerField()
    funcionarios_ativos = forms.IntegerField()
    trabalha_com_escala = forms.BooleanField(required=False)
    utiliza_banco_de_horas = forms.BooleanField(required=False)
    possui_control_id = forms.BooleanField(required=False)
    precisa_aplicativo = forms.BooleanField(required=False)
    precisa_de_facial = forms.BooleanField(required=False)
    possui_relogio_inmetro = forms.BooleanField(required=False)
    
