from rest_framework import serializers
from .models import Warga, Pengaduan

class WargaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warga
        fields = ['id', 'nik', 'nama_lengkap', 'alamat', 'no_telepon', 'tanggal_registrasi']

class PengaduanSerializer(serializers.ModelSerializer):
    pelapor_nama = serializers.CharField(source='pelapor.nama_lengkap', read_only=True)
    pelapor_nik = serializers.CharField(source='pelapor.nik', read_only=True)

    class Meta:
        model = Pengaduan
        fields = [
            'id', 'judul', 'deskripsi', 'status', 'tanggal_lapor',
            'pelapor', 'pelapor_nama', 'pelapor_nik'
        ]