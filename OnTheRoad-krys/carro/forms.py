from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from .models import *
from _projeto import settings

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


class FormularioAbastecimento(forms.ModelForm):
    data = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(FormularioAbastecimento, self).__init__(*args, **kwargs)
        self.fields['placa'] = CustomModelFilter(queryset=Veiculo.objects.filter(usuario=self.request.user))
    
    class Meta:
        model = Abastecer
        fields = ['placa', 'data', 'odometro', 'tipo_combustivel', 'qtd_litros', 'completo', 'preco', 'valor_total',
                  'posto']
        
    def clean_odometro(self):
        odometro = self.cleaned_data['odometro']
        carro = self.cleaned_data['placa']

        if carro.odometro > odometro:
            odometro_msg = "Odômetro menor do que o cadastrado!"
            raise ValidationError(odometro_msg)
        else:
            carro.odometro = odometro
            carro.save()
        
        return odometro

class FormularioDespesas(forms.ModelForm):
    data = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        print(self.request.user.veiculos)
        super(FormularioDespesas, self).__init__(*args, **kwargs)
        self.fields['placa'] = CustomModelFilter(queryset=Veiculo.objects.filter(usuario=self.request.user))
    class Meta:
        model = Despesa
        fields = ['placa', 'opcao','valor','odometro', 'data','local','observacao',]
    
    def clean_odometro(self):
        odometro = self.cleaned_data['odometro']
        carro = self.cleaned_data['placa']
        
        if carro.odometro > odometro:
            odometro_msg = "Odômetro menor do que o cadastrado!"
            raise ValidationError(odometro_msg)
        else:
            carro.odometro = odometro
            carro.save()
        
        return odometro

class FormularioTrocaOleo(forms.ModelForm):
    data = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(FormularioTrocaOleo, self).__init__(*args, **kwargs)
        self.fields['placa'] = CustomModelFilter(queryset=Veiculo.objects.filter(usuario=self.request.user))
    class Meta:
        model = Troca_Oleo
        fields = ['placa', 'data','km_atual','proxima_troca','filtro_oleo','placa']

    def clean_km_atual(self):
        km_atual = self.cleaned_data['km_atual']
        carro = self.cleaned_data['placa']
        
        if carro.odometro > km_atual:
            odometro_msg = "Odômetro menor do que o cadastrado!"
            raise ValidationError(odometro_msg)
        else:
            carro.odometro = km_atual
            carro.save()
        
        return km_atual