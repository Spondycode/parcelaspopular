from django.shortcuts import render, redirect
from .models import Parcela
from .forms import ParcelaForm, ParcelaFormSm
from django.http import HttpResponseRedirect

# Pagination requirements
from django.core.paginator import Paginator


# SHOW HOME PAGE
def home(request):
    return render(request, 'home.html', {})


# SHOW ABOUT PAGE
def about(request):
    return render(request, 'about.html', {})


# LIST ALL PARCELAS
def all_parcelas(request):
    parcela_list = Parcela.objects.all()

    # Pagination
    p = Paginator(Parcela.objects.all(), 2)
    page = request.GET.get('page')
    parcelas = p.get_page(page)
    nums = "a" * parcelas.paginator.num_pages

    return render(request, 'list_parcelas.html', {'parcela_list': parcela_list, 'parcelas': parcelas, 'nums': nums})


# SHOW ONE PARCELA
def show_parcela(request, parcela_id):    
    parcela = Parcela.objects.get(pk=parcela_id)
    return render(request, "show_parcela.html", {"parcela": parcela})


# UPDATE PARCELA
def update_parcela(request, parcela_id):
    parcela = Parcela.objects.get(pk=parcela_id)
    form = ParcelaForm(request.POST or None, instance=parcela)
    if form.is_valid():
        form.save()
        return redirect("all-parcelas")
    return render(request, "update_parcela.html", {"parcela": parcela, "form": form})


# ADD NEW pARCELA
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



