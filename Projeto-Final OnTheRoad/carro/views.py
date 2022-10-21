from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .forms import *
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

def principal(request):
    return render(request, 'inicial.html')

class Cadastrar_veiculo(LoginRequiredMixin, CreateView):
    model = Veiculo
    form_class = FormularioVeiculo
    success_url = reverse_lazy('carro:cadastro_veiculo')
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
    success_url = reverse_lazy('carro:abastecer_veiculo')
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
    success_url = reverse_lazy('home')
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
    success_url = reverse_lazy('home')
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
    return render(request, 'carro/tela.html')

def logout_view(request):
    logout(request)
    return redirect('carro:inicial')