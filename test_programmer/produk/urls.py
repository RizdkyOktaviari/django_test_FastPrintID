from django.urls import path

from . import views

app_name = 'produk'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('add/', views.AddProduk.as_view(), name='add'),
]