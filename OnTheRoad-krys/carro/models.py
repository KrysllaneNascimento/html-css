from enum import auto
from tabnanny import verbose
from django.db import models
from accounts.models import User

class TipoCombustivel(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Veiculo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="veiculos")
    marca = models.CharField(max_length=20)
    nome = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    placa = models.CharField(max_length=9)
    ano = models.IntegerField()
    tanque = models.IntegerField()
    tipo_combustivel = models.ForeignKey(TipoCombustivel, on_delete=models.DO_NOTHING, related_name='veiculos', verbose_name='Tipo de combustível')
    odometro = models.FloatField('Odômetro')
    renavam = models.CharField(max_length=11)

    def __str__(self):
        return self.placa

class Abastecer(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    placa = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    data = models.DateField()
    odometro = models.FloatField('Odômetro')
    tipo_combustivel = models.ForeignKey(TipoCombustivel, on_delete=models.DO_NOTHING, verbose_name='Tipo de combustível')
    qtd_litros = models.FloatField('Litros abastecidos')
    completo = models.BooleanField(default=False)
    preco = models.FloatField('Preço')
    valor_total = models.FloatField()
    posto = models.CharField(max_length=20)

class TipoDespesa(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Despesa(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    placa = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    opcao = models.ForeignKey(TipoDespesa, on_delete=models.DO_NOTHING, verbose_name='Tipo de despesa')
    valor = models.FloatField()
    odometro = models.FloatField('Odômetro')
    data = models.DateField()
    local = models.CharField(max_length=50)
    observacao = models.CharField('Observação' ,max_length=144, blank=True)

    def __str__(self):
        return self.observacao

class Troca_Oleo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    placa = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    data = models.DateField()
    km_atual = models.FloatField('KM atual')
    proxima_troca = models.FloatField('Próxima troca')
    filtro_oleo = models.BooleanField(default=True)