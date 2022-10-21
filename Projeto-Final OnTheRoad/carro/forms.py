from django import forms
from django.forms import ModelForm
from .models import *

class FormularioVeiculo(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(FormularioVeiculo, self).__init__(*args, **kwargs)
    class Meta:
        model = Veiculo
        fields = ['marca','nome','modelo','placa','ano','tanque','tipo_combustivel','odometro','renavam',]


class CustomModelFilter(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % (obj.placa)


class FormularioAbastecimento(ModelForm):
    filtro_oleo = forms.BooleanField(widget=forms.CheckboxInput, required=False, initial=False, label='Encheo o tanque: ')  

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(FormularioAbastecimento, self).__init__(*args, **kwargs)
        self.fields['placa'] = CustomModelFilter(queryset=Veiculo.objects.filter(usuario=self.request.user))
    class Meta:
        model = Abastecer
        fields = ['placa', 'data', 'odometro', 'tipo_combustivel', 'qtd_litros', 'completo', 'preco', 'valor_total',
                  'posto']
        

class FormularioDespesas(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        print(self.request.user.veiculos)
        super(FormularioDespesas, self).__init__(*args, **kwargs)
        self.fields['placa'] = CustomModelFilter(queryset=Veiculo.objects.filter(usuario=self.request.user))
    class Meta:
        model = Despesa
        fields = ['placa', 'opcao','valor','odometro', 'data','local','observacao',]
    

class FormularioTrocaOleo(forms.ModelForm):
    filtro_oleo = forms.BooleanField(widget=forms.CheckboxInput, required=False, initial=False, label='Troca de óleo: ')  

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(FormularioTrocaOleo, self).__init__(*args, **kwargs)
        self.fields['placa'] = CustomModelFilter(queryset=Veiculo.objects.filter(usuario=self.request.user))
    class Meta:
        model = Troca_Oleo
        fields = ['placa', 'data','km_atual','proxima_troca','filtro_oleo']
