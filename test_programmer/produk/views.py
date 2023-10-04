from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from produk.models import Produk
from produk.models import Kategori
from produk.models import Status
from produk.ProdukForm import ProdukForm, KategoriForm, StatusForm
from django.shortcuts import render, redirect

class Home(ListView):
    queryset = Produk.objects.all()
    template_name = 'layouts/index.html'

# view Produk
class Index(ListView):
    queryset = Produk.objects.all()
    template_name = 'produk/index.html' 

class AddProduk(CreateView):
    form_class = ProdukForm
    template_name = 'produk/add.html'
    success_url = reverse_lazy('produk:index_produk')

class EditProduk(UpdateView):
    model = Produk
    form_class = ProdukForm
    template_name = 'produk/edit.html'
    success_url = reverse_lazy('produk:index_produk')

def delete_produk(request, produk_id):
    produk = Produk.objects.get(id=produk_id)
    produk.delete()
    return redirect('produk:index_produk')

# view Kategori
class IndexKategori(ListView):
    queryset = Kategori.objects.all()
    template_name = 'kategori/index.html'

class AddKategori(CreateView):
    form_class = KategoriForm
    template_name = 'kategori/add.html'
    success_url = reverse_lazy('produk:index_kategori')

class EditKategori(UpdateView):
    model = Kategori
    form_class = KategoriForm
    template_name = 'kategori/edit.html'
    success_url = reverse_lazy('produk:index_kategori')

def delete_kategori(request, kategori_id):
    kategori = Kategori.objects.get(id=kategori_id)
    kategori.delete()
    return redirect('produk:index_kategori')

# view Status
class IndexStatus(ListView):
    queryset = Status.objects.all()
    template_name = 'status/index.html'

class AddStatus(CreateView):
    form_class = StatusForm
    template_name = 'status/add.html'
    success_url = reverse_lazy('produk:index_status')

class EditStatus(UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'status/edit.html'
    success_url = reverse_lazy('produk:index_status')

def delete_status(request, status_id):
    status = Status.objects.get(id=status_id)
    status.delete()
    return redirect('produk:index_status')