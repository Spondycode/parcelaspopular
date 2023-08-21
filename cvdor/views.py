from django.shortcuts import render, redirect
from .models import Parcela
from .forms import ParcelaForm, ParcelaFormSm
from django.http import HttpResponseRedirect


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



# def update_parcela(request, parcela_id):
#     parcela = Parcela.objects.get(pk=parcela_id)
#     form = ParcelaForm(request.POST or None)
#     if request.method == "POST":
#         form = ParcelaForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/update_parcela?submitted=True')
#     else:
#         form = ParcelaForm
#         if 'submitted' in request.GET:
#             submitted = True
#     return render(request, 'update_parcela.html', {"form": form, 'submitted': submitted})



def update_parcela(request, parcela_id):
    parcela = Parcela.objects.get(pk=parcela_id)
    form = ParcelaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("all-parcelas")
    return render(request, "update_parcela.html", {"parcela": parcela, "form": form})



# Add a new Parcela
def add_parcela(request):
    submitted = False
    if request.method == "POST":
        form = ParcelaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_parcela?submitted=True')
    else:
        form = ParcelaForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_parcela.html', {"form": form, 'submitted': submitted})



