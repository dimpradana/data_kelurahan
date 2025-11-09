from rest_framework import serializers
from .models import Warga
from .models import Pengaduan
from rest_framework import serializers
from .models import Warga, Pengaduan

class PengaduanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pengaduan
        fields = ['id', 'warga', 'judul', 'isi_laporan', 'tanggal_lapor', 'status']


class WargaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warga
        fields = '__all__'

class PengaduanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pengaduan
        fields = '__all__'




