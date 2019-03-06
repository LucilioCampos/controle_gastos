from django.shortcuts import render, redirect
from django.utils.datetime_safe import datetime
from .models import Transacao, Categoria
from .forms import TransacaoForm


def home(request):
    data = {'now': datetime.now(), 'after': datetime.now()}
    return render(request, 'home.html', data)


def listagem(request):
    data = {'transacoes': Transacao.objects.all()}
    return render(request, 'listagem.html', data)


def novaTransacao(request):
    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    return render(request, 'form.html', {'form': form})

def editar(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    data = {'form': form, 'transacao': transacao}
    return render(request, 'form.html', data)


def delete(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()
    return redirect('url_listagem')