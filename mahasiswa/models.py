from django.db import models

class GrupMahasiswa(models.Model):
    """Model untuk mengelompokkan mahasiswa berdasarkan kategori tertentu"""
    TIPE_GRUP_CHOICES = [
        ('KELAS', 'Kelas'),
        ('ORGANISASI', 'Organisasi'),
        ('KOMUNITAS', 'Komunitas'),
        ('PROJECT', 'Project Team'),
        ('LAINNYA', 'Lainnya'),
    ]
    
    nama_grup = models.CharField(max_length=100)
    tipe_grup = models.CharField(max_length=20, choices=TIPE_GRUP_CHOICES, default='KELAS')
    deskripsi = models.TextField(blank=True, null=True)
    tahun_dibuat = models.IntegerField()
    aktif = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Grup Mahasiswa'
        verbose_name_plural = 'Grup Mahasiswa'
        ordering = ['-tahun_dibuat', 'nama_grup']
    
    def __str__(self):
        return f"{self.nama_grup} ({self.get_tipe_grup_display()})"
    
    def jumlah_anggota(self):
        # Ubah dari mahasiswa_set menjadi mahasiswa (sesuai related_name)
        return self.mahasiswa.count()

class Mahasiswa(models.Model):
    nama = models.CharField(max_length=100)
    nim = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    jurusan = models.CharField(max_length=100)
    angkatan = models.IntegerField()
    alamat = models.TextField(blank=True, null=True)
    telepon = models.CharField(max_length=15, blank=True, null=True)
    foto = models.ImageField(upload_to='mahasiswa_photos/', blank=True, null=True)
    
    # Relasi Many-to-Many dengan Grup
    grup = models.ManyToManyField(GrupMahasiswa, blank=True, related_name='mahasiswa')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Mahasiswa'
        verbose_name_plural = 'Mahasiswa'
        ordering = ['nama']
    
    def __str__(self):
        return f"{self.nama} ({self.nim})"