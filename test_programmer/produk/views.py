from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from produk.models import Produk
from produk.models import Kategori
from produk.models import Status

class Index(ListView):
    queryset = Produk.objects.all()
    template_name = 'produk/index.html'
    

class AddProduk(CreateView):
    model = Produk
    fields = ['nama_produk', 'harga', 'kategori', 'status']
    template_name = 'produk/add.html'
    success_url = reverse_lazy('produk:index')
