from django import forms
from .models import Warga

class WargaForm(forms.ModelForm):
    class Meta:
        model = Warga
        fields = ['nik', 'nama_lengkap', 'alamat', 'no_telepon']
        
from .models import Pengaduan

class PengaduanForm(forms.ModelForm):
    class Meta:
        model = Pengaduan
        fields = ['judul', 'deskripsi', 'status', 'pelapor']