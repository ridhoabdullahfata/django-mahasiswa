from django.contrib import admin
from .models import Mahasiswa, GrupMahasiswa

@admin.register(GrupMahasiswa)
class GrupMahasiswaAdmin(admin.ModelAdmin):
    list_display = ['nama_grup', 'tipe_grup', 'tahun_dibuat', 'aktif', 'jumlah_anggota']
    list_filter = ['tipe_grup', 'aktif', 'tahun_dibuat']
    search_fields = ['nama_grup', 'deskripsi']
    list_editable = ['aktif']
    ordering = ['-tahun_dibuat', 'nama_grup']
    
    fieldsets = (
        ('Informasi Grup', {
            'fields': ('nama_grup', 'tipe_grup', 'tahun_dibuat', 'aktif')
        }),
        ('Deskripsi', {
            'fields': ('deskripsi',),
            'classes': ('collapse',)
        }),
    )

@admin.register(Mahasiswa)
class MahasiswaAdmin(admin.ModelAdmin):
    list_display = ['nama', 'nim', 'jurusan', 'angkatan', 'email']
    list_filter = ['jurusan', 'angkatan', 'grup']
    search_fields = ['nama', 'nim', 'email']
    filter_horizontal = ['grup']
    
    fieldsets = (
        ('Informasi Pribadi', {
            'fields': ('nama', 'nim', 'email', 'telepon')
        }),
        ('Informasi Akademik', {
            'fields': ('jurusan', 'angkatan', 'grup')
        }),
        ('Informasi Tambahan', {
            'fields': ('alamat', 'foto'),
            'classes': ('collapse',)
        }),
    )