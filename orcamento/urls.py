from django.urls import path
from app_orcamento import views

urlpatterns = [
    path('', views.fazer_login, name='login'),
    path('cadastro/', views.cadastro_usuario, name='cadastro'),
    path('home/', views.home, name='home')
]
