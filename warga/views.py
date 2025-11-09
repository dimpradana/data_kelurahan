
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Warga, Pengaduan
from .forms import WargaForm, PengaduanForm
from .serializers import WargaSerializer, PengaduanSerializer
from django.shortcuts import render



class WargaListView(ListView):
    model = Warga
    template_name = 'warga/warga_list.html'
    context_object_name = 'warga_list'

class WargaDetailView(DetailView):
    model = Warga
    template_name = 'warga/warga_detail.html'


class PengaduanListView(ListView):
    model = Pengaduan
    template_name = 'warga/pengaduan_list.html'
    context_object_name = 'pengaduan_list'
    ordering = ['-tanggal_lapor']


class WargaCreateView(CreateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga-list')


class PengaduanCreateView(CreateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan-list')

class WargaUpdateView(UpdateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga-list')

class WargaDeleteView(DeleteView):
    model = Warga
    template_name = 'warga/warga_confirm_delete.html'
    success_url = reverse_lazy('warga-list')

class PengaduanUpdateView(UpdateView):
    model = Pengaduan
    form_class = PengaduanForm  
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan-list')

class PengaduanDeleteView(DeleteView):
    model = Pengaduan
    template_name = 'warga/pengaduan_confirm_delete.html'
    success_url = reverse_lazy('pengaduan-list')

class WargaListAPIView(ListAPIView):
    queryset = Warga.objects.all()
    serializer_class = WargaSerializer

class WargaDetailAPIView(RetrieveAPIView):
    queryset = Warga.objects.all()
    serializer_class = WargaSerializer

class WargaViewSet(viewsets.ModelViewSet):
    queryset = Warga.objects.all().order_by('-tanggal_registrasi')
    serializer_class = WargaSerializer

class PengaduanViewSet(viewsets.ModelViewSet):

    queryset = Pengaduan.objects.all().order_by('-tanggal_lapor')  
    serializer_class = PengaduanSerializer

def index(request):
    warga_list = Warga.objects.all()
    return render(request, 'warga/warga_list.html', {'warga_list': warga_list})


def pengaduan_list(request):
    pengaduan_list = Pengaduan.objects.all().order_by('-tanggal_lapor')
    return render(request, 'warga/pengaduan_list.html', {'pengaduan_list': pengaduan_list})

