from django.contrib import admin
from .models import Warga, Pengaduan

admin.site.register(Warga)

@admin.register(Pengaduan)
class PengaduanAdmin(admin.ModelAdmin):
    list_display = ('judul', 'pelapor', 'status', 'tanggal_lapor')
    list_filter = ('status', 'tanggal_lapor')