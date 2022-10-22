from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
import carro.models as models
import email
import smtplib
from django.contrib.auth.decorators import login_required

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

class Trocar_Oleo(LoginRequiredMixin, CreateView):
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


@login_required(login_url='/login/')
def exibir_dados(request, placa_nome):
    user = request.user.id
    usuario = get_object_or_404(User, id=user)
    carro = get_object_or_404(Veiculo, usuario_id=user, placa=placa_nome)
    id_placa = carro.id
    abastecimentos = Abastecer.objects.filter(usuario_id=user, placa_id=id_placa)
    proxima_troca_oleo = Troca_Oleo.objects.filter(placa_id=id_placa)
    despesas_totais = Despesa.objects.filter(usuario_id=user, placa_id=id_placa)
    despesas_totais_lista = []
    despesas_totais_abastecimentos = []
    lista_odo = []
    lista_qtd = []
    for i in abastecimentos:
        lista_odo.append(i.odometro)
        despesas_totais_abastecimentos.append(i.valor_total)
    for j in abastecimentos:
        lista_qtd.append(j.qtd_litros)
    lista_odometro = []
    for i in despesas_totais:
        despesas_totais_lista.append(i.valor)

    despesas_totais_soma = sum(despesas_totais_lista)
    despesas_abastecimetos_soma = sum(despesas_totais_abastecimentos)
    lista_litros = []
    inicial = []
    for i in abastecimentos:
        lista_odometro.append(i.odometro)
    lista_odometro.reverse()
    lista_cont = []
    if len(lista_odometro) > 0:
        odometro_recente = lista_odometro[0]
    else:
        odometro_recente = 'Você ainda não cadastrou o seu odômetro'
    proximas_trocas = []
    verificador= []
    mensagem_media = ''
    for j in proxima_troca_oleo[::-1]:
        proximas_trocas.append(j.proxima_troca)
    proximas_trocas.reverse()
    if len(proximas_trocas) > 0:
        conta = proximas_trocas[-1] - lista_odometro[0]
        if conta > 1:
            mensagem_oleo = f'Faltam {conta} km para a próxima troca de óleo.'
            odometro_recente = lista_odometro[0]

        elif conta == 1:
            mensagem_oleo = f'Falta {conta} km para a próxima troca'
        else:
            mensagem_oleo = 'Você já pode realizar sua troca de óleo.'

            def enviar_email():
                corpo_email = """
                       <p>Olá amigo, você é um amigo</p>
                       """
                msg = email.message.Message()
                msg['Subject'] = f"Opa {usuario.nome}, tudo bem? Você já pode fazer a sua troca de óleo!!!"
                msg['From'] = 'ontheroad.suporte@gmail.com'
                msg['To'] = str(usuario.email)
                senha = 'taeyyjjhbbjubdno'
                msg.add_header('Content-Type', 'text/html')
                msg.set_payload(corpo_email)
                s = smtplib.SMTP('smtp.gmail.com: 587')
                s.starttls()
                s.login(msg['From'], senha)
                s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
                print('Email enviado')

            enviar_email()
    else:
        mensagem_oleo = 'Troca de óleo não cadastrada'
    while True:
            for i in abastecimentos[::-1]:
                if i.completo == True:
                    inicial.append(i.odometro)
                    lista_litros.append(i.qtd_litros)
                    lista_cont.append(i.completo)
                if i.completo == False:
                    lista_litros.append(i.qtd_litros)
                elif len(lista_cont) == 2:
                    inicial.append(i.odometro)
                    lista_litros.remove(lista_litros[-1])
                    break
            if len(lista_cont) <= 1:
                    mensagem_media = 'Média incalculável'
            else:
                for j in abastecimentos:
                    verificador.append(j.completo)
                if verificador[-1] == True:
                    soma = sum(lista_litros)
                    calculo = float(inicial[0]) - float(inicial[1])
                    mensagem_media = float(calculo) / float(soma)
                else:
                    mensagem_media = 'Média incalculável.'
            break

    context = {'usuario': usuario, 'carro': carro, 'mensagem_media':mensagem_media, 'odometro_recente':odometro_recente, 'mensagem_oleo':mensagem_oleo
               , 'despesas_totais_soma': despesas_totais_soma, 'despesas_abastecimentos_soma': despesas_abastecimetos_soma, 'abastecimentos': abastecimentos
               ,'proxima_troca_oleo': proxima_troca_oleo, 'despesas_totais': despesas_totais}

    return render(request, 'carro/exibir_dados.html',context)
