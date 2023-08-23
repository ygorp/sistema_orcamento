from django.urls import path
from app_orcamento import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('home/', views.home, name='home'),
    path('cadastro/', views.cadastro_usuario, name='cadastro'),
    path('', views.fazer_login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
