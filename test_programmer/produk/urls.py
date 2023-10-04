from django.urls import path

from . import views

app_name = 'produk'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    # Kategori
    path('index_kategori/', views.IndexKategori.as_view(), name='index_kategori'),
    path('add_kategori/', views.AddKategori.as_view(), name='add_kategori'),
    path('edit_kategori/<pk>', views.EditKategori.as_view(), name='edit_kategori'),
    path('delete_kategori/<int:kategori_id>/', views.delete_kategori, name='delete_kategori'),
    # Produk
    path('index_produk/', views.Index.as_view(), name='index_produk'),
    path('add_produk/', views.AddProduk.as_view(), name='add_produk'),
    path('edit_produk/<pk>', views.EditProduk.as_view(), name='edit_produk'),
    path('delete_produk/<int:produk_id>/', views.delete_produk, name='delete_produk'),
    # Status
    path('index_status/', views.IndexStatus.as_view(), name='index_status'),
    path('add_status/', views.AddStatus.as_view(), name='add_status'),
    path('edit_status/<pk>', views.EditStatus.as_view(), name='edit_status'),
    path('delete_status/<int:status_id>/', views.delete_status, name='delete_status'),
]