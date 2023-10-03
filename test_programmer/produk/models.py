from django.db import models


# Create your models here.

class Status(models.Model):
    
    nama_status = models.CharField(max_length=255)

    def __str__(self):
        return self.nama_status

class Kategori(models.Model):
    nama_kategori = models.CharField(max_length=255)

    def __str__(self):
        return self.nama_kategori
    
class Produk(models.Model):
    from .models  import Status  
    from .models  import Kategori  

    nama_produk = models.CharField(max_length=255)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_produk
