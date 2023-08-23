from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
