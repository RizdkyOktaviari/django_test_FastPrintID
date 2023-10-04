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

    def form_valid(self, form):
        nama_produk = form.cleaned_data['nama_produk']
        harga = form.cleaned_data['harga']
        
        # Cek panjang nama_produk
        if len(nama_produk) > 100:
            form.add_error('nama_produk', 'Nama produk terlalu panjang. Maksimal 100 karakter.')
            return self.form_invalid(form)

        # Cek apakah nama_produk sudah ada
        if Produk.objects.filter(nama_produk=nama_produk).exists():
            form.add_error('nama_produk', 'Nama produk sudah ada.')
            return self.form_invalid(form)
        
        if harga < 0:
            form.add_error('harga', 'Harga tidak boleh kurang dari 0.')
            return self.form_invalid(form)
        
        return super().form_valid(form)
    
        

class EditProduk(UpdateView):
    model = Produk
    form_class = ProdukForm
    template_name = 'produk/edit.html'
    success_url = reverse_lazy('produk:index_produk')

    def form_valid(self, form):
        nama_produk = form.cleaned_data['nama_produk']
        harga = form.cleaned_data['harga']
        
        # Cek panjang nama_produk
        if len(nama_produk) > 100:
            form.add_error('nama_produk', 'Nama produk terlalu panjang. Maksimal 100 karakter.')
            return self.form_invalid(form)

        # Cek apakah nama_produk sudah ada
        if Produk.objects.filter(nama_produk=nama_produk).exclude(id=self.object.id).exists():
            form.add_error('nama_produk', 'Nama produk sudah ada.')
            return self.form_invalid(form)
        
        if harga < 0:
            form.add_error('harga', 'Harga tidak boleh kurang dari 0.')
            return self.form_invalid(form)
        
        return super().form_valid(form)

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

    def form_valid(self, form):
        nama_kategori = form.cleaned_data['nama_kategori']
        
        # Cek panjang nama_kategori
        if len(nama_kategori) > 100:
            form.add_error('nama_kategori', 'Nama kategori terlalu panjang. Maksimal 100 karakter.')
            return self.form_invalid(form)

        # Cek apakah nama_kategori sudah ada
        if Kategori.objects.filter(nama_kategori=nama_kategori).exists():
            form.add_error('nama_kategori', 'Nama kategori sudah ada.')
            return self.form_invalid(form)
        
        return super().form_valid(form)

class EditKategori(UpdateView):
    model = Kategori
    form_class = KategoriForm
    template_name = 'kategori/edit.html'
    success_url = reverse_lazy('produk:index_kategori')

    def form_valid(self, form):
        nama_kategori = form.cleaned_data['nama_kategori']
        
        # Cek panjang nama_kategori
        if len(nama_kategori) > 100:
            form.add_error('nama_kategori', 'Nama kategori terlalu panjang. Maksimal 100 karakter.')
            return self.form_invalid(form)

        # Cek apakah nama_kategori sudah ada
        if Kategori.objects.filter(nama_kategori=nama_kategori).exclude(id=self.object.id).exists():
            form.add_error('nama_kategori', 'Nama kategori sudah ada.')
            return self.form_invalid(form)
        
        return super().form_valid(form)

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

    def form_valid(self, form):
        nama_status = form.cleaned_data['nama_status']
        
        # Cek panjang nama_status
        if len(nama_status) > 100:
            form.add_error('nama_status', 'Nama status terlalu panjang. Maksimal 100 karakter.')
            return self.form_invalid(form)

        # Cek apakah nama_status sudah ada
        if Status.objects.filter(nama_status=nama_status).exists():
            form.add_error('nama_status', 'Nama status sudah ada.')
            return self.form_invalid(form)
        
        return super().form_valid(form)

class EditStatus(UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'status/edit.html'
    success_url = reverse_lazy('produk:index_status')

    def form_valid(self, form):
        nama_status = form.cleaned_data['nama_status']
        
        # Cek panjang nama_status
        if len(nama_status) > 100:
            form.add_error('nama_status', 'Nama status terlalu panjang. Maksimal 100 karakter.')
            return self.form_invalid(form)

        # Cek apakah nama_status sudah ada
        if Status.objects.filter(nama_status=nama_status).exclude(id=self.object.id).exists():
            form.add_error('nama_status', 'Nama status sudah ada.')
            return self.form_invalid(form)
        
        return super().form_valid(form)

def delete_status(request, status_id):
    status = Status.objects.get(id=status_id)
    status.delete()
    return redirect('produk:index_status')