from django.db import models
from django.utils.datetime_safe import datetime


class Categoria(models.Model):
    nome = models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nome


class Transacao(models.Model):
    data = models.DateTimeField(default=datetime.now())
    updated_at = models.DateTimeField(default=datetime.now())
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    #um pra muitos
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    observacoes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Transações"

    def __str__(self):
        return self.descricao
