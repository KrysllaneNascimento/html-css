from django.db import models
from accounts.models import User

class TipoCombustivel(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Veiculo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="veiculos")
    marca = models.CharField(max_length=20)
    nome = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    placa = models.CharField(max_length=9)
    ano = models.IntegerField()
    tanque = models.IntegerField()
    tipo_combustivel = models.ForeignKey(TipoCombustivel, on_delete=models.DO_NOTHING)
    odometro = models.FloatField()
    renavam = models.CharField(max_length=11)

    def __str__(self):
        return self.placa

class Abastecer(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    placa = models.ForeignKey(Veiculo, on_delete=models.DO_NOTHING)
    data = models.CharField(max_length=10)
    odometro = models.FloatField()
    tipo_combustivel = models.ForeignKey(TipoCombustivel, on_delete=models.DO_NOTHING)
    qtd_litros = models.FloatField()
    completo = models.BooleanField(default=False)
    preco = models.FloatField()
    valor_total = models.FloatField()
    posto = models.CharField(max_length=20)

class TipoDespesa(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Despesa(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    placa = models.ForeignKey(Veiculo, on_delete=models.DO_NOTHING)
    opcao = models.ForeignKey(TipoDespesa, on_delete=models.DO_NOTHING)
    valor = models.FloatField()
    odometro = models.FloatField()
    data = models.CharField(max_length=10)
    local = models.CharField(max_length=50)
    observacao = models.CharField(max_length=144, blank=True)

    def __str__(self):
        return self.observacao

class Troca_Oleo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    placa = models.ForeignKey(Veiculo, on_delete=models.DO_NOTHING)
    data = models.CharField(max_length=10)
    km_atual = models.FloatField()
    proxima_troca = models.FloatField()
    filtro_oleo = models.BooleanField(default=True)