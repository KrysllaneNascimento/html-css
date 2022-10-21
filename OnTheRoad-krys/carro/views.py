from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
import carro.models as models

def principal(request):
    return render(request, 'inicial.html')

def todos(request):
    return render(request, 'carro/equipe.html')

def krys(request):
    return render(request, 'carro/krysllane.html')

def gabri(request):
    return render(request, 'carro/gabriel.html')

def adil(request):
    return render(request, 'carro/adilson.html')

def lari(request):
    return render(request, 'carro/larissa.html')

def cauan(request):
    return render(request, 'carro/mark.html')

class Cadastrar_veiculo(LoginRequiredMixin, CreateView):
    model = Veiculo
    form_class = FormularioVeiculo
    success_url = reverse_lazy('carro:usuario')
    template_name = 'carro/cadastro_veiculo.html'
    login_url = '/login/'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)

        return url

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

class Abastecer_veiculo(LoginRequiredMixin, CreateView):
    model = Abastecer
    form_class = FormularioAbastecimento
    success_url = reverse_lazy('carro:usuario')
    template_name = 'carro/abastecimento.html'
    login_url = '/login/'

    def form_valid(self, form):
        form.instance.usuario = self.request.user

        url = super().form_valid(form)

        return url

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

class Despesas(LoginRequiredMixin, CreateView):
    model = Despesa
    form_class = FormularioDespesas
    success_url = reverse_lazy('carro:usuario')
    template_name = 'carro/despesas.html'
    login_url = '/login/'

    def form_valid(self, form):
        form.instance.usuario = self.request.user

        url = super().form_valid(form)

        return url

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

class Troca_Oleo(LoginRequiredMixin, CreateView):
    model = Troca_Oleo
    form_class = FormularioTrocaOleo
    success_url = reverse_lazy('carro:usuario')
    template_name = 'carro/troca_oleo.html'
    login_url = '/login/'

    def form_valid(self, form):
        form.instance.usuario = self.request.user

        url = super().form_valid(form)

        return url
        
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


def usuario(request):
    carros = request.user.veiculos.all()
    return render(request, 'carro/usuario.html', {'usuario': request.user, 'carros': carros})


def logout_view(request):
    logout(request)
    return redirect('carro:inicial')


def exibir_dados(request, placa_nome):
    user = request.user.id
    usuario = get_object_or_404(User, id=user)
    carro = get_object_or_404(Veiculo, usuario_id=user, placa=placa_nome)
    id_placa = carro.id
    dados_abast = Abastecer.objects.filter(usuario_id=user, placa_id=id_placa)
    despesas = Despesa.objects.filter(usuario_id=user, placa_id=id_placa)
    trocas_oleo = models.Troca_Oleo.objects.filter(usuario_id=user, placa_id=id_placa)
    lista_odo = []
    lista_qtd = []
    valores_totais = []
    valores_abastecimentos = []
    valores_despesas = []
    for i in dados_abast:
        lista_odo.append(i.odometro)
    for i in dados_abast:
        lista_qtd.append(i.qtd_litros)

    for i in despesas:
        valores_totais.append(i.valor)
        valores_despesas.append(i.valor)
    for i in dados_abast:
        valores_totais.append(i.valor_total)
        valores_abastecimentos.append((i.valor_total))
    despesas_totais = sum(valores_totais)
    despesas_abastecimento = sum(valores_abastecimentos)
    despesas_carro = sum(valores_despesas)

    if carro.odometro < 10000: 
        km_faltante = 10000 - carro.odometro
    else:
        km_excedente = carro.odometro % 10000
        print(carro.odometro)
        km_faltante = 10000 - km_excedente

    context = {'usuario': usuario, 'carro': carro, 'despesas_totais': despesas_totais, 'despesas_abastecimento': despesas_abastecimento, 'despesas_carro': despesas_carro, 'troca_oleo': km_faltante, 'abastecimentos': dados_abast, 'despesas': despesas, 'trocas_oleo': trocas_oleo}
    return render(request, 'carro/exibir_dados.html', context)
