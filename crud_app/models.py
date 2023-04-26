from django.db import models

# Create your models here.


class Posts(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='images/')
    data_criacao = models.DateTimeField(auto_now_add=True)
