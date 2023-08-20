from django.shortcuts import render
from .models import Parcela
from .forms import ParcelaForm, ParcelaFormSm


def home(request):
    return render(request, 'home.html', {})


def about(request):
    return render(request, 'about.html', {})


def all_parcelas(request):
    parcela_list = Parcela.objects.all()
    return render(request, 'list_parcelas.html', {'parcela_list': parcela_list})


def show_parcela(request, parcela_id):
    parcela = Parcela.objects.get(pk=parcela_id)
    return render(request, "show_parcela.html", {"parcela": parcela})



def update_parcela(request, parcela_id):
    parcela = Parcela.objects.get(pk=parcela_id)
    form = ParcelaFormSm(request.POST or None)
    return render(request, "update_parcela.html", {"parcela": parcela, "form": form})


