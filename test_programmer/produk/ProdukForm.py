from django import forms
from .models import Produk, Kategori, Status

class ProdukForm(forms.ModelForm):
    class Meta:
        model = Produk
        fields = ['nama_produk', 'harga', 'kategori', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Mengambil data dari database
        self.fields['kategori'].choices = [(k.id, k.nama_kategori) for k in Kategori.objects.all()]
        self.fields['status'].choices = [(s.id, s.nama_status) for s in Status.objects.all()]

class KategoriForm(forms.ModelForm):
    class Meta:
        model = Kategori
        fields = ['nama_kategori']

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['nama_status']

