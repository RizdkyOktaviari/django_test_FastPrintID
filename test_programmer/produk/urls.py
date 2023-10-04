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
    # API Produk
    path('api/produk/', views.ProdukApi.as_view(), name='produk-list'),
    path('api/add_produk/' , views.ProdukCreateApi.as_view(), name='produk-create'),
    path('api/edit_produk/<int:pk>/', views.ProdukUpdateApi.as_view(), name='produk-update'),
    path('api/delete_produk/<int:pk>/', views.ProdukDeleteApi.as_view(), name='produk-delete'),
    # API Kategori
    path('api/kategori/', views.KategoriApi.as_view(), name='kategori-list'),
    path('api/add_kategori/' , views.KategoriCreateApi.as_view(), name='kategori-create'),
    path('api/edit_kategori/<int:pk>/', views.KategoriUpdateApi.as_view(), name='kategori-update'),
    path('api/delete_kategori/<int:pk>/', views.KategoriDeleteApi.as_view(), name='kategori-delete'),
    # API Status
    path('api/status/', views.StatusApi.as_view(), name='status-list'),
    path('api/add_status/' , views.StatusCreateApi.as_view(), name='status-create'),
    path('api/edit_status/<int:pk>/', views.StatusUpdateApi.as_view(), name='status-update'),
    path('api/delete_status/<int:pk>/', views.StatusDeleteApi.as_view(), name='status-delete'),

]