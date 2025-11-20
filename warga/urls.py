from django.urls import path
from .views import (
    WargaListView, WargaDetailView, WargaCreateView, 
    WargaUpdateView, WargaDeleteView,
    PengaduanListView, PengaduanCreateView, PengaduanUpdateView, PengaduanDeleteView
)

urlpatterns = [
    # Warga URLs
    path('', WargaListView.as_view(), name='warga_list'),
    path('tambah/', WargaCreateView.as_view(), name='warga_tambah'),
    path('<int:pk>/', WargaDetailView.as_view(), name='warga_detail'),
    path('<int:pk>/edit/', WargaUpdateView.as_view(), name='warga_edit'),
    path('<int:pk>/hapus/', WargaDeleteView.as_view(), name='warga_hapus'),
    
    # Pengaduan URLs
    path('pengaduan/', PengaduanListView.as_view(), name='pengaduan_list'),
    path('pengaduan/tambah/', PengaduanCreateView.as_view(), name='pengaduan_tambah'),
    path('pengaduan/<int:pk>/edit/', PengaduanUpdateView.as_view(), name='pengaduan_edit'),
    path('pengaduan/<int:pk>/hapus/', PengaduanDeleteView.as_view(), name='pengaduan_hapus'),
]