from django.urls import path
from app_orcamento import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('cadastro/', views.cadastro_usuario, name='cadastro'),
    path('', views.fazer_login, name='login'),
]
