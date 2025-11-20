from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Warga, Pengaduan
from .forms import WargaForm, PengaduanForm
from .serializers import WargaSerializer, PengaduanSerializer


# ===== HTML VIEWS (CBV) =====
class WargaListView(ListView):
    model = Warga
    template_name = 'warga/warga_list.html'
    context_object_name = 'warga_list'

class WargaDetailView(DetailView):
    model = Warga
    template_name = 'warga/warga_detail.html'

class WargaCreateView(CreateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga-list')

class WargaUpdateView(UpdateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga-list')

class WargaDeleteView(DeleteView):
    model = Warga
    template_name = 'warga/warga_confirm_delete.html'
    success_url = reverse_lazy('warga-list')

class PengaduanListView(ListView):
    model = Pengaduan
    template_name = 'warga/pengaduan_list.html'
    context_object_name = 'pengaduan_list'

class PengaduanCreateView(CreateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan-list')

class PengaduanUpdateView(UpdateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan-list')

class PengaduanDeleteView(DeleteView):
    model = Pengaduan
    template_name = 'warga/pengaduan_confirm_delete.html'
    success_url = reverse_lazy('pengaduan-list')


# ===== API VIEWS (DRF) =====
class WargaViewSet(viewsets.ModelViewSet):
    queryset = Warga.objects.all().order_by('-tanggal_registrasi')
    serializer_class = WargaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Konfigurasi filtering, searching, ordering
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {
        'nama_lengkap': ['exact', 'contains'],
        'nik': ['exact', 'contains'],
    }
    search_fields = ['nama_lengkap', 'nik', 'alamat']
    ordering_fields = ['nama_lengkap', 'tanggal_registrasi']
    ordering = ['-tanggal_registrasi']  # Default ordering


class PengaduanViewSet(viewsets.ModelViewSet):
    queryset = Pengaduan.objects.all().order_by('-tanggal_lapor')
    serializer_class = PengaduanSerializer
    permission_classes = [IsAuthenticated]

    # Konfigurasi filtering, searching, ordering
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {
        'judul': ['exact', 'contains'],
        'status': ['exact'],
        'pelapor__nama_lengkap': ['exact', 'contains'],
    }
    search_fields = ['judul', 'deskripsi', 'pelapor__nama_lengkap']
    ordering_fields = ['judul', 'status', 'tanggal_lapor']
    ordering = ['-tanggal_lapor']  # Default ordering
# Default ordering