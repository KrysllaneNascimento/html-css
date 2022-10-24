from django.contrib import admin
from . models import *

class VeiculoAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'marca', 'nome', 'modelo', 'placa', 'ano', 'tanque', 'tipo_combustivel', 'odometro', 'renavam']
    list_editable = ['marca', 'nome', 'modelo', 'placa', 'ano', 'tanque', 'tipo_combustivel', 'odometro', 'renavam']

class TipoCombustivelAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    list_editable = ['nome']

class AbastecerAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'placa', 'data', 'odometro', 'tipo_combustivel', 'qtd_litros', 'completo', 'preco', 'valor_total', 'posto']
    list_editable = ['placa', 'data', 'odometro', 'tipo_combustivel', 'qtd_litros', 'completo', 'preco', 'valor_total', 'posto']

class TipoDespesaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    list_editable = ['nome']

class DespesaAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'placa', 'opcao', 'valor', 'odometro', 'data', 'local', 'observacao']
    list_editable = ['placa', 'opcao', 'valor', 'odometro', 'data', 'local', 'observacao']

class TrocaOleoAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario','placa', 'data', 'km_atual', 'proxima_troca', 'filtro_oleo', 'placa']
    list_editable = ['placa', 'data', 'km_atual', 'proxima_troca', 'filtro_oleo', 'placa']

admin.site.register(Veiculo, VeiculoAdmin)
admin.site.register(TipoCombustivel, TipoCombustivelAdmin)
admin.site.register(Abastecer, AbastecerAdmin)
admin.site.register(TipoDespesa, TipoDespesaAdmin)
admin.site.register(Despesa, DespesaAdmin)
admin.site.register(Troca_Oleo, TrocaOleoAdmin)