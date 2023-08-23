# sistema_orcamento
Projeto para uso interno da empresa, feito para gerar orçamento de sistemas de ponto!

## Capturas de Tela
![Tela de Login](/static/img/login.png)
![Tela de Cadastro](/static/img/cadastro.png)
![Tela de Inicio](/static/img/home.png)

## Tecnologias Utilizadas

- Python
- Django
- HTML
- CSS
- JavaScript

## Configuração

1. Clone o repositório:
2. git clone https://github.com/seu-usuario/sistema_orcamento.git
3. Crie a virtual env:
     - windows = python -m venv venv
     - Linux = python3 -m venv venv
4. Ative o ambiente virtual:
     - Windows = venv/Scripts/Activate
     - Linux = source venv/bin/activate
5. Instale as dependências:
     - pip install django;
     - pip install mysqlclient;
     - pip install django-cors-headers
6. Execute as migrações:
     - python manage.py migrate
7. Execute o servidor de desenvolvimento:
     - python manage.py runserver
8. Acesse o aplicativo no seu navegador em `http://127.0.0.1:8000/`.

## Funcionalidades
  - **Gerar Orçamento:** Página que permite aos usuários preencher um formulário para gerar um orçamento com base nas opções selecionadas.

## Estrutura de Diretórios

    nome-do-projeto/
    ├── nome-do-app/
    │ ├── migrations/
    │ ├── static/
    │ │ ├── css/
    │ │ ├── js/
    │ ├── templates/
    │ ├── admin.py
    │ ├── forms.py
    │ ├── models.py
    │ ├── urls.py
    │ ├── views.py
    ├── nome-do-projeto/
    │ ├── settings.py
    │ ├── urls.py
    ├── manage.py
