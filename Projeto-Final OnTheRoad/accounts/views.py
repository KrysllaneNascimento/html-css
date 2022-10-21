from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from .forms import UsuarioRegistrarForm

def cadastro(request):
    """
    Função de cadastrar usuários. Se o método da requisição for POST, irá preencher o formulário de cadastro de usuário,
    salvará o usuário e fará login. Se não for um POST, a função devolverá um formulário vazio para o usuário preencher.
    """
    if request.method == 'POST':
        form = UsuarioRegistrarForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('home')
    
    form = UsuarioRegistrarForm()
    return render(request,'registration/registro.html', {'form':form})