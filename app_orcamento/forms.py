from django import forms


class OrcamentoForm(forms.Form):
    nome_cliente = forms.CharField(max_length=100)
    cnpj = forms.CharField(max_length=20)
    possui_control_id = forms.BooleanField(required=False)
    precisa_aplicativo = forms.BooleanField(required=False)
    possui_relogio_inmetro = forms.BooleanField(required=False)
    funcionarios_ativos = forms.IntegerField()
